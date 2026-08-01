import subprocess, os
os.chdir(r"D:\sunny-E\SWX\Download\saas-ai-blog")
# 本地构建测试
result = subprocess.run("hugo --gc --minify", shell=True, capture_output=True, text=True, encoding="utf-8")
print("STDOUT:", result.stdout[-3000:] if result.stdout else "")
print("STDERR:", result.stderr[-3000:] if result.stderr else "")
print("Return code:", result.returncode)
if result.returncode == 0:
    print("\n✅ Hugo 构建成功！内链问题已解决")
else:
    print("\n❌ Hugo 构建仍有错误")