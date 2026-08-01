import requests
import re
url = "https://saas-ai-blog.netlify.app/blog/2026-07-31-framer-guide/"
resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
html = resp.text
# 提取 head 部分
head = html[:html.find("</head>")]
print("=== HEAD 部分 ===")
print(head[:3000])
print("\n=== 检查 meta description ===")
m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', html)
if m:
    print(f"✅ 找到 description: {m.group(1)}")
else:
    print("❌ 没有找到 description meta 标签")
    # 看看有没有其他形式的 description
    m2 = re.search(r'description[^>]*', html)
    if m2:
        print(f"   找到相关内容: {m2.group(0)}")
    else:
        print("   完全没有任何 description 相关内容")