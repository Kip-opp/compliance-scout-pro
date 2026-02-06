from fpdf import FPDF
from datetime import datetime

class AuditReport(FPDF):
    def header(self):
        # Professional Header
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "AI COMPLIANCE SCOUT - SECURITY AUDIT", border=False, ln=True, align="C")
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
        self.ln(10)

    def footer(self):
        # Professional Footer
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf_report(repo_url, audit_results):
    pdf = AuditReport()
    pdf.add_page()
    
    # Summary Section
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, f"Target Repository: {repo_url}", ln=True)
    pdf.ln(5)
    
    # Results Section
    pdf.set_font("helvetica", "", 10)
    for file_path, result in audit_results.items():
        pdf.set_font("helvetica", "B", 10)
        pdf.set_fill_color(240, 240, 240) # Light gray background for file headers
        pdf.cell(0, 8, f"FILE: {file_path}", ln=True, fill=True)
        
        pdf.set_font("helvetica", "", 9)
        # multi_cell handles long text and automatic line breaks
        pdf.multi_cell(0, 5, result)
        pdf.ln(5)

    report_name = "Security_Audit_Report.pdf"
    pdf.output(report_name)
    print(f"✅ Report saved as: {report_name}")