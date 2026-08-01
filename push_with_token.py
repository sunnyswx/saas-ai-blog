import subprocess
import os
SITE_DIR = r"C:\Users\wxsu\aipywork\CZsHXUB5Usoy1cWcGyWVA\saas-ai-blog"
os.chdir(SITE_DIR)
# 恢复HTTPS remote
subprocess.run(["git", "remote", "set-url", "origin", "https://github.com/sunnyswx/saas-ai-blog.git"], capture_output=True)
# 检查是否配置了git credential
print("🔍 检查 Git 凭证配置...")
result = subprocess.run(["git", "config", "--global", "credential.helper"], capture_output=True, text=True)
print(f"   credential.helper: {result.stdout.strip() or '未配置'}")
# 尝试用 GIT_TERMINAL_PROMPT=0 来避免交互式认证
print("\n🔄 尝试推送（使用默认凭证）...")
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"
result = subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True, timeout=30, env=env)
print(f"   输出: {result.stdout}")
if result.stderr:
    print(f"   stderr: {result.stderr}")
if result.returncode == 0:
    print("\n✅✅✅ 推送成功！")
else:
    print(f"\n❌ 推送失败 (code: {result.returncode})")
    # 检查是否是认证问题
    if "403" in result.stderr or "Authentication" in result.stderr:
        print("\n🔑 需要认证。请提供 GitHub 个人访问令牌 (Personal Access Token)")
        print("   1. 访问 https://github.com/settings/tokens 创建 token")
        print("   2. 运行以下命令设置 token：")
        print('      git remote set-url origin https://<TOKEN>@github.com/sunnyswx/saas-ai-blog.git')
        print("   3. 然后运行：git push origin master")
    elif "443" in result.stderr or "Could not connect" in result.stderr:
        print("\n🌐 网络连接问题，可能是代理或防火墙限制")
        print("   尝试设置代理：")
        print('      git config --global http.proxy http://127.0.0.1:7890')
        print('      git config --global https.proxy http://127.0.0.1:7890')
        print("   然后重新运行：git push origin master")
    else:
        print(f"\n💡 请手动运行以下命令推送：")
        print(f"   cd {SITE_DIR}")
        print(f"   git push origin master")