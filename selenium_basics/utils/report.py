import os
from datetime import datetime

class HtmlReport:
    def __init__(self, report_name="test_report.html"):
        self.report_dir = "reports"
        os.makedirs(self.report_dir, exist_ok=True)
        self.report_path = os.path.join(self.report_dir, report_name)
        self.entries = []

    def log_pass(self, url, expected, actual):
        self.entries.append(
            f"<tr style='color:green'><td>{url}</td><td>{expected}</td><td>{actual}</td><td>PASS</td></tr>"
        )

    def log_fail(self, url, expected, actual, screenshot_path):
        self.entries.append(
            f"<tr style='color:red'><td>{url}</td><td>{expected}</td>"
            f"<td>{actual}</td><td>FAIL<br>{screenshot_path}</td></tr>"
        )

    def generate(self):
        with open(self.report_path, "w", encoding="utf-8") as f:
            f.write("<html><body>")
            f.write("<h2>QA Automation Test Report</h2>")
            f.write("<table border='1' cellpadding='5'>")
            f.write("<tr><th>URL</th><th>Expected</th><th>Actual</th><th>Status</th></tr>")
            for entry in self.entries:
                f.write(entry)
            f.write("</table></body></html>")

        print(f"HTML report generated at: {self.report_path}")
