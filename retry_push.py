import subprocess
import os
SITE_DIR = r"C:\Users\wxsu\aipywork\CZsHXUB5Usoy1cWcGyWVA\saas-ai-blog"
os.chdir(SITE_DIR)
print("🔍 检查网络连接...")
# 测试网络连通性
result = subprocess.run(["ping", "-n", "1", "github.com"], capture_output=True, text=True, timeout=10)
print(f"ping github.com: {'✅ 通' if result.returncode == 0 else '❌ 不通'}")
# 查看当前git remote配置
result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
print(f"\n📌 Git remote 配置:\n{result.stdout}")
# 尝试用SSH方式推送（如果配置了SSH key）
print("\n🔄 尝试用 SSH 方式推送...")
ssh_url = "git@github.com:sunnyswx/saas-ai-blog.git"
result = subprocess.run(["git", "remote", "set-url", "origin", ssh_url], capture_output=True, text=True)
print(f"   设置 SSH remote: {'✅' if result.returncode == 0 else '❌'}")
result = subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True, timeout=30)
print(f"   SSH 推送结果:\n{result.stdout}")
if result.stderr:
    print(f"   {result.stderr}")
if result.returncode == 0:
    print("\n✅✅✅ SSH 推送成功！")
else:
    print("\n❌ SSH 也失败了，恢复为HTTPS...")
    subprocess.run(["git", "remote", "set-url", "origin", "https://github.com/sunnyswx/saas-ai-blog.git"], capture_output=True)
    print("\n💡 建议：在浏览器中打开 https://github.com/sunnyswx/saas-ai-blog 查看提交状态")
    print(f"   commit 已成功创建: feat: add internal links between blog posts")
    print(f"   等网络恢复后，运行以下命令推送：")
    print(f"   cd {SITE_DIR}")
    print(f"   git push origin master")