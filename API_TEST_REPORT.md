# Product Hunt API 测试报告

## 测试日期
2026-08-05

## 1. API 端点
```
https://api.producthunt.com/v2/api/graphql
```

## 2. 认证方式
```
Authorization: Bearer [TOKEN]
Content-Type: application/json
```

## 3. 正确的参数

### 排序选项
| 参数 | 值 | 说明 |
|------|-----|------|
| `order` | `VOTES` | 按投票数排序 |
| `order` | `NEWEST` | 按创建时间排序 |
| `order` | `FEATURED_AT` | 按推荐时间排序 |
| `order` | `RANKING` | 按排名排序 |

### 分页
- `first`: 返回数量
- `after`: 游标（base64 编码的数字）

## 4. Post 对象字段

### 核心字段
| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | String | 产品 ID |
| `name` | String | 产品名称 |
| `tagline` | String | 产品简介 |
| `description` | String | 产品描述 |
| `votesCount` | Int | 投票数 |
| `createdAt` | DateTime | 创建时间 |
| `website` | String | 产品网站 |
| `url` | String | Product Hunt 链接 |
| `slug` | String | URL 友好名称 |

### 排名字段
| 字段 | 类型 | 说明 |
|------|------|------|
| `dailyRank` | Int | 当日排名 |
| `weeklyRank` | Int | 周排名 |
| `monthlyRank` | Int | 月排名 |
| `yearlyRank` | Int | 年排名 |

### 话题字段
```graphql
topics {
  nodes {
    name
  }
}
```

### 评论字段
```graphql
comments(first: 5) {
  edges {
    node {
      id
      body
      createdAt
    }
  }
}
```

## 5. 不存在的参数

| 参数 | 状态 | 建议 |
|------|------|------|
| `filter` | ❌ 不存在 | 无法按日期/主题筛选 |
| `search` | ❌ 不存在 | 无搜索功能 |
| `orderBy` | ❌ 错误 | 应使用 `order` |
| `tags` | ❌ 不存在 | 应使用 `topics` |

## 6. 测试查询示例

### 基础查询
```graphql
{
  posts(first: 20, order: VOTES) {
    edges {
      node {
        id
        name
        tagline
        votesCount
        createdAt
        website
        description
        topics {
          nodes {
            name
          }
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

### 单个产品详情
```graphql
{
  post(id: "1181193") {
    id
    name
    tagline
    votesCount
    createdAt
    website
    description
    topics {
      nodes {
        name
      }
    }
    comments(first: 5) {
      edges {
        node {
          id
          body
          createdAt
        }
      }
    }
  }
}
```

## 7. 已知限制

1. **无筛选功能**：无法按日期范围或主题筛选
2. **无搜索功能**：无法搜索产品名称
3. **分页限制**：最大返回 50 条（需分页获取）
4. **评论限制**：最多获取 100 条评论
5. **速率限制**：未测试，但存在限制

## 8. 数据质量

- ✅ 投票数真实（从 400+ 到 1000+）
- ✅ 时间戳格式正确
- ✅ 描述内容丰富
- ✅ 话题分类准确
- ⚠️ 评论数据可能不完整

## 9. 可用话题

从测试结果中提取的话题：
- Productivity
- Artificial Intelligence
- Developer Tools
- Marketing
- Sales
- SEO
- Open Source
- SaaS
- Design Tools
- Video
- Education
- 等...

## 10. 建议

1. 使用 `order: VOTES` 获取热门产品
2. 使用 `first: 50` 获取最多数据
3. 通过分页获取更多数据
4. 在客户端筛选 SaaS 相关产品
5. 手动验证佣金数据
