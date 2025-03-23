# Subdomain Scanner Tool

A powerful Python-based tool for discovering subdomains of target domains using multiple discovery methods including DNS enumeration and certificate transparency logs.

## Features

- DNS enumeration with concurrent scanning
- Certificate transparency logs scanning via crt.sh
- Custom wordlist support
- Multithreaded scanning for better performance
- Output results to file

## Prerequisites

- Python 3.8 or higher installed on your system
- pip (Python package installer)
- Basic command line knowledge

### Required Dependencies
The following Python packages will be automatically installed via requirements.txt:
- dnspython (>= 2.3.0) - For DNS enumeration and resolution
- requests (>= 2.31.0) - For HTTP requests and certificate transparency logs
- tqdm (>= 4.65.0) - For progress bar visualization
- flask (>= 3.0.0) - For web interface functionality

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd subdomain-scanner
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

#### Basic Command Structure
```bash
python subdomain_scanner.py -d DOMAIN -w WORDLIST [-t THREADS] [-o OUTPUT]
```

#### Command Line Arguments

- `-d, --domain`: Target domain to scan (required)
- `-w, --wordlist`: Path to the wordlist file containing subdomain prefixes (required)
- `-t, --threads`: Number of concurrent threads (optional, default: 10)
- `-o, --output`: Output file to save results (optional)

#### Examples

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

### Web Interface

#### Starting the Web Server

1. Start the Flask web server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`

#### Using the Web Interface

1. Enter the target domain in the domain input field
2. (Optional) Adjust the number of threads
3. (Optional) Upload a custom wordlist file
4. Click the "Scan" button to start the scan
5. View results in real-time as they appear
6. Download the results using the "Download Results" button

#### Features

- User-friendly interface for subdomain scanning
- Real-time display of discovered subdomains
- Adjustable thread count for performance optimization
- Optional custom wordlist upload
- Easy download of scan results

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