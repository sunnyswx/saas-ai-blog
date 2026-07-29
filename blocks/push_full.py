import subprocess
import os
SITE_DIR = r"C:\Users\wxsu\aipywork\CZsHXUB5Usoy1cWcGyWVA\saas-ai-blog"
GITHUB_URL = "https://github.com/sunnyswx/saas-ai-blog.git"
os.chdir(SITE_DIR)
print("🚀 重新推送...\n")
# 1. 先看看当前分支
branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
print(f"📌 当前分支: {branch.stdout.strip() or '无'}")
# 2. 查看所有分支
branches = subprocess.run(["git", "branch", "-a"], capture_output=True, text=True)
print(f"📋 所有分支:\n{branches.stdout}")
# 3. 检查是否有任何提交
log = subprocess.run(["git", "log", "--oneline"], capture_output=True, text=True)
if log.stdout.strip():
    print(f"✅ 已有提交:\n{log.stdout}")
else:
    print("⚠️ 没有提交记录，需要先创建第一个提交")
    # 创建第一个提交
    # 先确保有文件
    result = subprocess.run(["git", "add", "--all"], capture_output=True, text=True)
    print(f"📦 git add: {result.stdout}")
    # 提交
    result = subprocess.run(["git", "commit", "-m", "Initial commit: AI Tools Hub blog"], capture_output=True, text=True)
    print(f"💾 git commit: {result.stdout}")
    if result.returncode != 0:
        print(f"❌ 提交失败: {result.stderr}")
        # 尝试设置默认分支
        subprocess.run(["git", "config", "init.defaultBranch", "main"], capture_output=True)
        print("✅ 已设置默认分支为 main")
        # 再次提交
        result = subprocess.run(["git", "commit", "-m", "Initial commit: AI Tools Hub blog"], capture_output=True, text=True)
        print(f"💾 git commit (重试): {result.stdout}")
# 4. 推送到 GitHub
print("\n📤 推送到 GitHub...")
result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
print(f"📡 推送结果: {result.stdout}")
if result.stderr:
    print(f"   stderr: {result.stderr}")
if result.returncode == 0:
    print("\n✅✅✅ 推送成功！")
    print(f"   GitHub 仓库: {GITHUB_URL}")
else:
    print(f"\n❌ 推送失败")
    # 尝试 master 分支
    print("尝试 master 分支...")
    result = subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ 推送成功 (master 分支)!")
    else:
        print(f"❌ 还是失败: {result.stderr}")
        print("\n💡 可能原因：")
        print("   1. 需要输入 GitHub 账号密码")
        print("   2. 或者需要设置 Personal Access Token")
        print("   3. 请确认仓库已创建: https://github.com/sunnyswx/saas-ai-blog")
utils.set_state(success=True)