import csv

def generate_report(vulnerabilities, output_file="report.csv"):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Vulnerability"])
        for vuln in vulnerabilities:
            writer.writerow([vuln['url'], vuln['payload']])
