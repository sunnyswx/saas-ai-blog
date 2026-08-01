import os, subprocess
repo_dir = r"C:\Users\s\Documents\Netfily\saas-ai-blog"
os.chdir(repo_dir)
# 检查 git log 看最近的提交
result = subprocess.run(["git", "log", "--oneline", "-3"], capture_output=True, text=True)
print("📋 最近提交记录：")
print(result.stdout)
# 检查远程状态
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print("📋 当前状态：")
print(result.stdout)
# 尝试再次推送
print("🚀 重新推送...")
result = subprocess.run(["git", "push"], capture_output=True, text=True, encoding="utf-8", errors="replace")
print(result.stdout)
if result.stderr:
    print(result.stderr[:500])
if result.returncode == 0:
    print("✅ 推送成功！")
else:
    print(f"❌ 推送失败，返回码: {result.returncode}")