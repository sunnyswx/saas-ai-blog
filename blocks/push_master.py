import subprocess
import os
SITE_DIR = r"C:\Users\wxsu\aipywork\CZsHXUB5Usoy1cWcGyWVA\saas-ai-blog"
os.chdir(SITE_DIR)
print("🚀 推送到 GitHub (master 分支)...\n")
result = subprocess.run(["git", "push", "-u", "origin", "master"], capture_output=True, text=True)
print(f"📡 推送输出:\n{result.stdout}")
if result.stderr:
    print(f"   stderr: {result.stderr}")
if result.returncode == 0:
    print("\n✅✅✅ 推送成功！")
    print(f"   GitHub 仓库: https://github.com/sunnyswx/saas-ai-blog")
    print(f"   网站: https://saas-ai-blog.netlify.app")
else:
    print(f"\n❌ 推送失败")
    print("💡 可能是需要 GitHub 身份验证")
    print("   请尝试手动运行以下命令：")
    print(f'   cd "{SITE_DIR}"')
    print("   git push -u origin master")
utils.set_state(success=True)