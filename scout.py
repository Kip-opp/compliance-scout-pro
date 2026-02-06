import os
from git import Repo
import shutil

def clone_and_scan(repo_url):
    # This is where the downloaded code will sit temporarily
    local_path = "./target_code"
    
    # 1. Clean up old runs
    if os.path.exists(local_path):
        shutil.rmtree(local_path)
    
    # 2. Clone the repo
    print(f"🚀 Scouting: {repo_url}")
    Repo.clone_from(repo_url, local_path)
    
    # 3. Identify 'High-Value' files for security auditing
    # These are the files where developers usually hide secrets or make mistakes
    targets = ['.env', 'config', 'database', 'auth', 'settings']
    found_files = []

    for root, dirs, files in os.walk(local_path):
        for file in files:
            # We want config files or main logic files (.py, .js, .ts)
            if any(t in file.lower() for t in targets) or file.endswith(('.py', '.js')):
                found_files.append(os.path.join(root, file))

    print(f"✅ Scout found {len(found_files)} critical files.")
    return found_files

if __name__ == "__main__":
    # Test it with a public repository
    test_url = "https://github.com/django/django" 
    files = clone_and_scan(test_url)
    for f in files[:10]: # Print the first 10 files found
        print(f"📍 Target: {f}")