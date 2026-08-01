import subprocess
import os
os.chdir(r"D:\sunny-E\SWX\Download\saas-ai-blog")
def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8")
    print(f"$ {cmd}")
    if result.stdout:
        print(result.stdout[:2000])
    if result.stderr:
        print("STDERR:", result.stderr[:1000])
    print("---")
    return result
# 1. 检查状态
run("git status")
# 2. 添加文件
run("git add content/blog/2026-07-31-framer-guide.md content/blog/2026-07-31-framer-vs-webflow-wordpress.md content/blog/2026-07-31-framer-advanced-tips.md")
# 3. 检查暂存状态
run("git status")
# 4. 提交
run('git commit -m "add 3 framer articles: beginner guide, comparison, advanced tips"')
# 5. 推送
result = run("git push origin main")
if result.returncode != 0:
    # 尝试 master 分支
    result = run("git push origin master")
print("=== DONE ===")