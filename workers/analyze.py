import subprocess

def analyze_pr(pr_id, changed_files):
    results = {}
    for file in changed_files:
        if file.endswith(('.js', '.jsx')):
            try:
                output = subprocess.check_output(['flake8', file], text=True)
                results[file] = output if output else 'No issues found'
            except subprocess.CalledProcessError as e:
                results[file] = f'Errors: {e.output}'
    return results

# Mock PR data for now
if __name__ == "__main__":
    print(analyze_pr(1, ['test.js']))