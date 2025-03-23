from flask import Flask, render_template, request, jsonify, send_file
from subdomain_scanner import SubdomainScanner
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    domain = request.form.get('domain')
    threads = int(request.form.get('threads', 10))
    wordlist_file = request.files.get('wordlist')
    
    if not domain:
        return jsonify({'error': 'Domain is required'}), 400
    
    # Handle wordlist file if uploaded
    wordlist_path = None
    if wordlist_file:
        wordlist_path = os.path.join(os.path.dirname(__file__), 'temp_wordlist.txt')
        wordlist_file.save(wordlist_path)
    
    try:
        scanner = SubdomainScanner(domain, wordlist_path, threads)
        subdomains = scanner.scan()
        
        # Clean up temporary wordlist file
        if wordlist_path and os.path.exists(wordlist_path):
            os.remove(wordlist_path)
        
        # Save results to a file, removing duplicates
        sorted_subdomains = sorted(list(set(subdomains)))
        results_file = os.path.join(os.path.dirname(__file__), 'scan_results.txt')
        with open(results_file, 'w') as f:
            for subdomain in sorted_subdomains:
                f.write(subdomain + '\n')
        
        return jsonify({
            'success': True,
            'subdomains': sorted_subdomains,
            'count': len(sorted_subdomains),
            'has_results': True
        })
    except Exception as e:
        if wordlist_path and os.path.exists(wordlist_path):
            os.remove(wordlist_path)
        return jsonify({'error': str(e)}), 500

@app.route('/download')
def download():
    results_file = os.path.join(os.path.dirname(__file__), 'scan_results.txt')
    if not os.path.exists(results_file):
        return jsonify({'error': 'No scan results found'}), 404
    return send_file(results_file, as_attachment=True, download_name='scan_results.txt')

if __name__ == '__main__':
    app.run(debug=True)