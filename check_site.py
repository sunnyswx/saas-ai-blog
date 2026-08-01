import requests
import json
from urllib.parse import urljoin
BASE = "https://saas-ai-blog.netlify.app"
pages = [
    "/",
    "/blog/",
    "/blog/2026-07-31-framer-guide/",
    "/blog/2026-07-31-framer-vs-webflow-wordpress/",
    "/blog/2026-07-31-framer-advanced-tips/",
    "/blog/wispr-flow-review-real-experience/",
    "/blog/wispr-flow-tutorial-guide/",
    "/blog/wispr-flow-vs-traditional-voice-input/",
]
results = []
for path in pages:
    url = urljoin(BASE, path)
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        status = "✅" if resp.status_code == 200 else "❌"
        # 检查内容
        has_framer = "Framer" in resp.text or "framer" in resp.text
        has_affiliate = "framer.link/su-swx" in resp.text
        has_title = "<title>" in resp.text
        has_meta_desc = 'name="description"' in resp.text or 'name="Description"' in resp.text
        content_len = len(resp.text)
        results.append({
            "path": path,
            "status_code": resp.status_code,
            "status_icon": status,
            "has_framer_content": has_framer,
            "has_affiliate_link": has_affiliate,
            "has_title": has_title,
            "has_meta_desc": has_meta_desc,
            "content_length": content_len,
            "elapsed": round(resp.elapsed.total_seconds(), 2)
        })
    except Exception as e:
        results.append({
            "path": path,
            "status_code": str(e),
            "status_icon": "❌",
            "error": str(e)
        })
# 输出结果
print("=" * 80)
print(f"🌐 网站全面检查报告: {BASE}")
print("=" * 80)
for r in results:
    print(f"\n{r['status_icon']} {r['path']}")
    print(f"   HTTP状态: {r.get('status_code')}")
    if 'error' in r:
        print(f"   错误: {r['error']}")
    else:
        print(f"   响应时间: {r['elapsed']}s")
        print(f"   页面大小: {r['content_length']} bytes")
        print(f"   有标题: {'✅' if r['has_title'] else '❌'}")
        print(f"   有Meta描述: {'✅' if r['has_meta_desc'] else '❌'}")
        print(f"   包含Framer内容: {'✅' if r['has_framer_content'] else '❌'}")
        print(f"   包含联盟链接: {'✅' if r['has_affiliate_link'] else '❌'}")
# 检查内链是否可访问
print("\n" + "=" * 80)
print("🔗 内链检查（文章之间的互相引用）")
print("=" * 80)
# 检查 framer-guide 是否链接到其他两篇
guide_url = urljoin(BASE, "/blog/2026-07-31-framer-guide/")
try:
    resp = requests.get(guide_url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code == 200:
        has_link_to_vs = "framer-vs-webflow-wordpress" in resp.text
        has_link_to_tips = "framer-advanced-tips" in resp.text
        print(f"📘 framer-guide → 链接到对比文章: {'✅' if has_link_to_vs else '❌'}")
        print(f"📘 framer-guide → 链接到技巧文章: {'✅' if has_link_to_tips else '❌'}")
except:
    print("❌ 无法访问 framer-guide 页面检查内链")
print("\n" + "=" * 80)
print("📊 总结")
print("=" * 80)
success = [r for r in results if r.get('status_code') == 200]
failed = [r for r in results if r.get('status_code') != 200]
print(f"✅ 可访问页面: {len(success)}/{len(results)}")
print(f"❌ 不可访问页面: {len(failed)}/{len(results)}")
for f in failed:
    print(f"   - {f['path']}: {f.get('status_code')}")