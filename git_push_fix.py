import subprocess, os
os.chdir(r"D:\sunny-E\SWX\Download\saas-ai-blog")
def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(f"$ {cmd}")
    if result.stdout:
        print(result.stdout[:1500])
    if result.stderr:
        print("STDERR:", result.stderr[:800])
    print("---")
    return result
run("git add content/blog/2026-07-31-framer-guide.md content/blog/2026-07-31-framer-vs-webflow-wordpress.md content/blog/2026-07-31-framer-advanced-tips.md")
run('git commit -m "fix internal links: replace relref with absolute URLs to fix Netlify build"')
result = run("git push origin master")
print("=== DONE ===")