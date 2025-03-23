# Subdomain Scanner Tool Documentation

## Overview
The Subdomain Scanner is a powerful Python-based tool designed for discovering subdomains of target domains. It utilizes multiple discovery methods including DNS enumeration and certificate transparency logs to provide comprehensive scanning results.

## Prerequisites
- Python 3.x installed on your system
- pip (Python package installer)
- Basic command line knowledge

## Installation

1. Clone or download the repository to your local machine

2. Navigate to the project directory:
   ```bash
   cd subdomain-scanner
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Command Structure
```bash
python subdomain_scanner.py -d DOMAIN -w WORDLIST [-t THREADS] [-o OUTPUT]
```

### Command Line Arguments
- `-d, --domain`: Target domain to scan (required)
- `-w, --wordlist`: Path to the wordlist file containing subdomain prefixes (required)
- `-t, --threads`: Number of concurrent threads (optional, default: 10)
- `-o, --output`: Output file to save results (optional)

### Examples

1. Basic scan with default settings:
   ```bash
   python subdomain_scanner.py -d example.com -w wordlist.txt
   ```

2. Scan with increased thread count and save results:
   ```bash
   python subdomain_scanner.py -d example.com -w wordlist.txt -t 20 -o results.txt
   ```

3. Using a custom wordlist:
   ```bash
   python subdomain_scanner.py -d example.com -w custom_wordlist.txt -o scan_results.txt
   ```

## Output
The tool will display discovered subdomains in real-time during the scan. If an output file is specified, the results will be saved in the following format:
```
subdomain1.example.com
subdomain2.example.com
subdomain3.example.com
```

## Best Practices
1. Start with a smaller thread count and increase if needed
2. Use an appropriate wordlist size for your target
3. Always ensure you have permission to scan the target domain
4. Save your results using the output option for future reference

## Troubleshooting
- If the scan seems slow, try adjusting the thread count
- Ensure your wordlist file is properly formatted (one subdomain prefix per line)
- Check your internet connection if the scan fails to start

## Legal Notice
This tool is for educational and authorized testing purposes only. Always obtain proper authorization before scanning any domain. Unauthorized scanning may be illegal in your jurisdiction.

## Contributing
Contributions are welcome! Please feel free to submit pull requests or report issues to help improve the tool.