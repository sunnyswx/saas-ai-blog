import requests
import re
BASE = "https://saas-ai-blog.netlify.app"
pages = [
    "/",
    "/blog/",
    "/blog/2026-07-31-framer-guide/",
    "/blog/2026-07-31-framer-vs-webflow-wordpress/",
    "/blog/2026-07-31-framer-advanced-tips/",
    "/blog/wispr-flow-review-real-experience/",
]
print("=== Meta Description 全面复核（使用修正后的正则）===")
all_ok = True
for path in pages:
    url = BASE + path
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        html = resp.text
        # 修正正则：匹配 name=description 或 name="description"
        m = re.search(r'<meta\s+name=["\']?description["\']?\s+content=["\']([^"\']*)["\']', html)
        if m:
            desc = m.group(1)
            status = "✅"
            print(f"{status} {path}")
            print(f"     描述: {desc[:80]}...")
        else:
            all_ok = False
            print(f"❌ {path} 没有 description")
    except Exception as e:
        all_ok = False
        print(f"❌ {path} 访问失败: {e}")
print("\n" + "=" * 60)
print("✅ 所有页面 Meta Description 均正常！" if all_ok else "⚠️ 仍有页面缺少描述")