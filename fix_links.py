import re
import os
blog_dir = r"D:\sunny-E\SWX\Download\saas-ai-blog\content\blog"
# 定义映射：relref 引用 -> 实际 URL 路径
link_map = {
    '{{< relref "/blog/framer-guide" >}}': '/blog/2026-07-31-framer-guide/',
    '{{< relref "/blog/framer-vs-webflow-wordpress" >}}': '/blog/2026-07-31-framer-vs-webflow-wordpress/',
    '{{< relref "/blog/framer-advanced-tips" >}}': '/blog/2026-07-31-framer-advanced-tips/',
}
files = [
    "2026-07-31-framer-guide.md",
    "2026-07-31-framer-vs-webflow-wordpress.md",
    "2026-07-31-framer-advanced-tips.md",
]
for fname in files:
    fpath = os.path.join(blog_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    for old, new in link_map.items():
        content = content.replace(old, new)
    
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 已修复: {fname}")
    else:
        print(f"⚠️ 无需修改: {fname}")
print("\n=== 修复完成 ===")