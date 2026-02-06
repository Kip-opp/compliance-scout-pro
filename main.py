from scout import clone_and_scan
from auditor import audit_file
from reporter import generate_pdf_report

def run_full_audit(repo_url):
    print("🚀 Starting Professional Audit...")
    files_to_check = clone_and_scan(repo_url)
    
    all_results = {}
    
    # We check the first 3 files for the prototype
    for file in files_to_check[:3]:
        result = audit_file(file)
        all_results[file] = result
    
    # Generate the professional document
    generate_pdf_report(repo_url, all_results)

if __name__ == "__main__":
    url = input("Enter GitHub URL to audit: ")
    run_full_audit(url)