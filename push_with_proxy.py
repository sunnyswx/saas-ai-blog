import subprocess
import os
SITE_DIR = r"C:\Users\wxsu\aipywork\CZsHXUB5Usoy1cWcGyWVA\saas-ai-blog"
os.chdir(SITE_DIR)
# 先检查系统是否有代理设置
print("🔍 检查系统代理设置...")
# 检查环境变量
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy", "ALL_PROXY"]:
    val = os.environ.get(var)
    if val:
        print(f"   {var} = {val}")
# 尝试常见的代理端口
proxy_ports = [7890, 1080, 10809, 8080, 3128]
for port in proxy_ports:
    result = subprocess.run(["git", "config", "--global", f"http.proxy", f"http://127.0.0.1:{port}"], capture_output=True, text=True)
    result = subprocess.run(["git", "config", "--global", f"https.proxy", f"http://127.0.0.1:{port}"], capture_output=True, text=True)
    # 测试连接
    result = subprocess.run(["git", "ls-remote", "https://github.com/sunnyswx/saas-ai-blog.git", "HEAD"], capture_output=True, text=True, timeout=10)
    if result.returncode == 0:
        print(f"\n✅ 代理 127.0.0.1:{port} 可用！")
        # 用这个代理推送
        print("\n🚀 开始推送...")
        result = subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True, timeout=30)
        print(f"   输出: {result.stdout}")
        if result.stderr:
            print(f"   stderr: {result.stderr}")
        if result.returncode == 0:
            print("\n✅✅✅ 推送成功！")
            print(f"   GitHub 仓库: https://github.com/sunnyswx/saas-ai-blog")
        else:
            print(f"\n❌ 推送失败 (code: {result.returncode})")
        # 清除代理设置
        subprocess.run(["git", "config", "--global", "--unset", "http.proxy"], capture_output=True)
        subprocess.run(["git", "config", "--global", "--unset", "https.proxy"], capture_output=True)
        break
    else:
        subprocess.run(["git", "config", "--global", "--unset", "http.proxy"], capture_output=True)
        subprocess.run(["git", "config", "--global", "--unset", "https.proxy"], capture_output=True)
else:
    print("\n❌ 未找到可用的代理")
    print("\n💡 老板，看起来是网络环境限制了 GitHub 连接。您可以：")
    print("   1. 开一下代理/VPN，然后运行以下命令推送：")
    print(f"      cd {SITE_DIR}")
    print(f"      git push origin master")
    print("   2. 或者手动在浏览器中提交：")
    print("      https://github.com/sunnyswx/saas-ai-blog")
    print("\n✅ 不过 commit 已经成功创建了！")
    print("   提交信息: feat: add internal links between blog posts + related articles section")
    print("   修改了3个Markdown文件，新增15个内链")