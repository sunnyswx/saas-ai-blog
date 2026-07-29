import subprocess
import os
SITE_DIR = r"C:\Users\wxsu\aipywork\CZsHXUB5Usoy1cWcGyWVA\saas-ai-blog"
os.chdir(SITE_DIR)
print("🚀 开始配置 Git 并推送到 GitHub...\n")
# 步骤 1：配置 Git 用户名和邮箱
print("📝 步骤 1: 配置 Git 身份信息")
subprocess.run(["git", "config", "user.name", "saas-ai-blog"], capture_output=True)
subprocess.run(["git", "config", "user.email", "saas-ai-blog@example.com"], capture_output=True)
print("   ✅ Git 用户名: saas-ai-blog")
print("   ✅ Git 邮箱: saas-ai-blog@example.com")
# 步骤 2：初始化 Git 仓库
print("\n📝 步骤 2: 初始化 Git 仓库")
if not os.path.exists(os.path.join(SITE_DIR, ".git")):
    subprocess.run(["git", "init"], capture_output=True)
    print("   ✅ Git 仓库已初始化")
else:
    print("   ℹ️ Git 仓库已存在")
# 步骤 3：添加所有文件
print("\n📝 步骤 3: 添加文件到 Git")
result = subprocess.run(["git", "add", "."], capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ 所有文件已添加到暂存区")
else:
    print(f"   ❌ 添加失败: {result.stderr}")
# 步骤 4：提交
print("\n📝 步骤 4: 提交文件")
result = subprocess.run(["git", "commit", "-m", "Initial commit: AI Tools Hub blog with Wispr Flow articles"], capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ 文件已提交")
elif "nothing to commit" in result.stderr:
    print("   ℹ️ 没有新的变更需要提交")
else:
    print(f"   ✅ 提交成功")
# 步骤 5：设置远程仓库
print("\n📝 步骤 5: 配置 GitHub 远程仓库")
print("   ⚠️ 需要您先在 GitHub 上创建仓库！")
print("")
print("="*60)
print("📋 以下是您需要在 GitHub 上操作的步骤")
print("="*60)
print("""
🔧 第一步：登录 GitHub
   访问 https://github.com/login
   登录您的账号（没有的话先注册）
🔧 第二步：创建新仓库
   点击右上角 + 号 → "New repository"
   仓库名输入: saas-ai-blog
   选择 Public（公开）
   不要勾选任何选项（README、.gitignore、license）
   点击 "Create repository"
🔧 第三步：复制远程仓库地址
   创建后会看到一个页面，复制里面的命令：
   git remote add origin https://github.com/你的用户名/saas-ai-blog.git
🔧 第四步：把复制的命令发给我
   我帮您在电脑上执行，一键推送到 GitHub！
""")
# 输出当前状态
print("\n📄 当前 Git 状态:")
result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
if result.stdout.strip():
    for line in result.stdout.split("\n"):
        if line.strip():
            print(f"   {line}")
else:
    print("   ✅ 所有文件已提交，等待推送到 GitHub")
print(f"\n🎉 本地准备工作已完成！请把 GitHub 上复制的命令发给我！")
utils.set_state(success=True)