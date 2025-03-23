#!/usr/bin/env python3

import argparse
import dns.resolver
import concurrent.futures
import requests
from typing import List, Set
from tqdm import tqdm

class SubdomainScanner:
    def __init__(self, domain: str, wordlist: str = None, max_threads: int = 10):
        self.domain = domain
        self.wordlist = wordlist
        self.max_threads = max_threads
        self.subdomains: Set[str] = set()
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = 2
        self.resolver.lifetime = 2

    def dns_enumeration(self, subdomain: str) -> None:
        """Perform DNS enumeration for a given subdomain"""
        try:
            full_domain = f"{subdomain}.{self.domain}"
            self.resolver.resolve(full_domain, 'A')
            self.subdomains.add(full_domain)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
            pass
        except Exception as e:
            print(f"Error scanning {full_domain}: {str(e)}")

    def load_wordlist(self) -> List[str]:
        """Load subdomains from wordlist file"""
        try:
            with open(self.wordlist, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Error loading wordlist: {str(e)}")
            return []

    def scan_from_crt_sh(self) -> None:
        """Scan subdomains using crt.sh certificate transparency logs"""
        try:
            url = f"https://crt.sh/?q=%.{self.domain}&output=json"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for entry in data:
                    name_value = entry.get('name_value', '')
                    if name_value:
                        self.subdomains.add(name_value)
        except Exception as e:
            print(f"Error scanning crt.sh: {str(e)}")

    def scan(self) -> Set[str]:
        """Main scanning function"""
        print(f"\nStarting subdomain scan for {self.domain}...")

        # Scan using certificate transparency logs
        print("Scanning certificate transparency logs...")
        self.scan_from_crt_sh()

        # Scan using wordlist if provided
        if self.wordlist:
            print(f"Loading wordlist from {self.wordlist}...")
            wordlist = self.load_wordlist()
            if wordlist:
                print(f"Starting DNS enumeration with {len(wordlist)} subdomains...")
                with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                    list(tqdm(executor.map(self.dns_enumeration, wordlist), total=len(wordlist)))

        return self.subdomains

def main():
    parser = argparse.ArgumentParser(description='Subdomain Scanner Tool')
    parser.add_argument('-d', '--domain', required=True, help='Target domain to scan')
    parser.add_argument('-w', '--wordlist', help='Path to subdomain wordlist file')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of threads (default: 10)')
    parser.add_argument('-o', '--output', help='Output file to save results')
    args = parser.parse_args()

    scanner = SubdomainScanner(args.domain, args.wordlist, args.threads)
    subdomains = scanner.scan()

    print(f"\nFound {len(subdomains)} subdomains:")
    for subdomain in sorted(subdomains):
        print(subdomain)

    if args.output:
        try:
            with open(args.output, 'w') as f:
                for subdomain in sorted(subdomains):
                    f.write(f"{subdomain}\n")
            print(f"\nResults saved to {args.output}")
        except Exception as e:
            print(f"Error saving results: {str(e)}")

if __name__ == '__main__':
    main()