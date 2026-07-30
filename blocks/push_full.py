import subprocess
import os
SITE_DIR = r"C:\Users\wxsu\aipywork\CZsHXUB5Usoy1cWcGyWVA\saas-ai-blog"
GITHUB_URL = "https://github.com/sunnyswx/saas-ai-blog.git"
os.chdir(SITE_DIR)
print("🚀 开始推送修改到 GitHub...\n")
# 1. 查看当前分支
branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
current_branch = branch.stdout.strip()
print(f"📌 当前分支: {current_branch or '无'}")
# 2. 查看所有分支
branches = subprocess.run(["git", "branch", "-a"], capture_output=True, text=True)
print(f"📋 所有分支:\n{branches.stdout}")
# 3. 检查是否有任何提交
log = subprocess.run(["git", "log", "--oneline", "-5"], capture_output=True, text=True)
print(f"📜 最近提交:\n{log.stdout or '无提交'}")
# 4. 查看修改状态
status = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
print(f"📝 修改状态:\n{status.stdout or '无修改'}")
# 5. 查看具体修改了哪些文件
diff_files = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True)
print(f"📄 修改的文件:\n{diff_files.stdout or '无'}")
# 6. 添加所有修改
print("\n📝 步骤 1: git add .")
subprocess.run(["git", "add", "."], capture_output=True)
print("   ✅ 已暂存所有修改")
# 7. 提交
print("\n📝 步骤 2: git commit")
commit_msg = "feat: add internal links between blog posts + related articles section"
result = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
print(f"   {result.stdout}")
if result.stderr:
    print(f"   {result.stderr}")
# 8. 推送
print("\n📝 步骤 3: git push")
# 尝试推送当前分支
if current_branch:
    result = subprocess.run(["git", "push", "-u", "origin", current_branch], capture_output=True, text=True)
else:
    # 如果没有分支，尝试master
    result = subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True)
print(f"   {result.stdout}")
if result.stderr:
    print(f"   {result.stderr}")
if result.returncode == 0:
    print("\n✅✅✅ 推送成功！")
    print(f"   GitHub 仓库: https://github.com/sunnyswx/saas-ai-blog")
else:
    print(f"\n❌ 推送失败，returncode: {result.returncode}")
    # 尝试其他分支
    print("\n🔄 尝试推送到 main 分支...")
    result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
    print(f"   {result.stdout}")
    if result.stderr:
        print(f"   {result.stderr}")
    if result.returncode == 0:
        print("\n✅✅✅ 推送成功！")
    else:
        print("\n🔄 尝试推送到 master 分支...")
        result = subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True)
        print(f"   {result.stdout}")
        if result.stderr:
            print(f"   {result.stderr}")
        if result.returncode == 0:
            print("\n✅✅✅ 推送成功！")