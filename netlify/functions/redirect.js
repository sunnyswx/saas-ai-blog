const redirects = {
  "wisprflow": "https://ref.wisprflow.ai/sunny-nv3z",
  "wispr": "https://ref.wisprflow.ai/sunny-nv3z",
  "flow": "https://ref.wisprflow.ai/sunny-nv3z",
  "default": "https://ref.wisprflow.ai/sunny-nv3z",
};
exports.handler = async (event, context) => {
  const tool = event.path.replace("/.netlify/functions/redirect/", "").replace("/go/", "").toLowerCase();
  const targetUrl = redirects[tool] || redirects["default"];
  return {
    statusCode: 302,
    headers: {
      Location: targetUrl,
      "Cache-Control": "no-cache",
    },
  };
};
