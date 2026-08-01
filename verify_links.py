import os, glob
blog_dir = r"D:\sunny-E\SWX\Download\saas-ai-blog\content\blog"
# 检查是否还有 relref 残留
for f in glob.glob(os.path.join(blog_dir, "2026-07-31-framer*.md")):
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    relrefs = [line for line in content.splitlines() if "relref" in line]
    if relrefs:
        print(f"❌ {os.path.basename(f)} 仍有 relref: {relrefs}")
    else:
        print(f"✅ {os.path.basename(f)} 无 relref，内链已修复")
print("\n=== 验证完成 ===")