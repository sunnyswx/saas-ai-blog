# Product Hunt API 测试报告 v2

## 测试日期
2026-08-06

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

### 3.1 基础查询
```graphql
{
  posts(first: 20, order: VOTES) {
    edges {
      node {
        id, name, tagline, votesCount, createdAt
      }
    }
  }
}
```

### 3.2 排序选项 (PostsOrder)
| 值 | 说明 |
|---|------|
| `FEATURED_AT` | 按 featured 日期降序 |
| `VOTES` | 按投票数降序 |
| `RANKING` | 按排名降序 |
| `NEWEST` | 按创建时间降序 |

### 3.3 筛选参数
| 参数 | 类型 | 说明 |
|------|------|------|
| `postedAfter` | DateTime | 筛选在此日期之后发布的产品 |
| `postedBefore` | DateTime | 筛选在此日期之前发布的产品 |
| `topic` | String | 按主题 slug 筛选（如 "saas", "developer-tools"） |
| `featured` | Boolean | 是否只返回 featured 产品 |
| `url` | String | 按产品 URL 筛选 |
| `twitterUrl` | String | 按 Twitter URL 筛选 |

### 3.4 分页参数
| 参数 | 类型 | 说明 |
|------|------|------|
| `first` | Int | 返回数量 |
| `last` | Int | 从末尾返回数量 |
| `after` | String | 游标分页（起始） |
| `before` | String | 游标分页（结束） |

### 3.5 可用字段
| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | ID | 产品 ID |
| `name` | String | 产品名称 |
| `tagline` | String | 产品简介 |
| `description` | String | 产品描述 |
| `votesCount` | Int | 投票数 |
| `createdAt` | DateTime | 创建时间 |
| `website` | String | 产品网站 |
| `url` | String | PH 页面 URL |
| `dailyRank` | Int | 日排名 |
| `weeklyRank` | Int | 周排名 |
| `monthlyRank` | Int | 月排名 |
| `yearlyRank` | Int | 年排名 |
| `slug` | String | 产品 slug |
| `topics` | TopicConnection | 主题列表 |
| `comments` | CommentConnection | 评论列表 |
| `latestScore` | Int | 最新评分 |
| `makerReplies` | Int | 创作者回复数 |
| `reviewsCount` | Int | 评论数 |
| `reviewsRating` | Float | 评分 |

## 4. 正确的查询示例

### 4.1 获取今日热门产品（按投票数）
```graphql
{
  posts(first: 50, order: VOTES, postedAfter: "2026-08-06T00:00:00Z") {
    edges {
      node {
        id, name, tagline, votesCount, createdAt, dailyRank, weeklyRank
        topics { nodes { name } }
      }
    }
    pageInfo { hasNextPage endCursor }
  }
}
```

### 4.2 获取特定主题的产品（如 SaaS）
```graphql
{
  posts(first: 20, order: VOTES, topic: "saas") {
    edges {
      node {
        id, name, tagline, votesCount, createdAt, dailyRank
        topics { nodes { name } }
      }
    }
  }
}
```

### 4.3 获取特定日期的产品
```graphql
{
  posts(first: 20, order: NEWEST, 
        postedAfter: "2026-08-05T00:00:00Z",
        postedBefore: "2026-08-05T23:59:59Z") {
    edges {
      node {
        id, name, tagline, votesCount, createdAt, dailyRank, weeklyRank
        topics { nodes { name } }
      }
    }
  }
}
```

### 4.4 获取单个产品详情
```graphql
{
  post(id: "1181193") {
    id, name, tagline, description, website
    votesCount, createdAt, dailyRank, weeklyRank, monthlyRank
    topics { nodes { name } }
    comments(first: 10) {
      edges {
        node { id, body, createdAt }
      }
    }
  }
}
```

## 5. 主题 (Topic) 信息

### 5.1 获取所有主题
```graphql
{
  topics(first: 100) {
    edges {
      node {
        id, name, slug, postsCount, followersCount
      }
    }
  }
}
```

### 5.2 热门主题（按 followersCount）
| 主题名称 | Slug | Posts Count | Followers |
|---------|------|-------------|-----------|
| Notion | notion | 4167 | 2260 |
| NFT | nft | 953 | 2273 |
| Vibe coding | vibe-coding | 1204 | 603 |
| Inclusivity | inclusivity | 301 | 539 |
| Intimacy | intimacy | 227 | 413 |
| Vercel Day | vercel-day | 1559 | 32 |

### 5.3 筛选 SaaS 产品
```graphql
{
  posts(first: 20, order: VOTES, topic: "saas") {
    edges {
      node {
        id, name, tagline, votesCount
        topics { nodes { name } }
      }
    }
  }
}
```

## 6. API 功能总结

### 6.1 支持的筛选
- ✅ 按投票数排序 (`order: VOTES`)
- ✅ 按最新排序 (`order: NEWEST`)
- ✅ 按排名排序 (`order: RANKING`)
- ✅ 按日期筛选 (`postedAfter`, `postedBefore`)
- ✅ 按主题筛选 (`topic: "saas"`)
- ✅ 只返回 featured 产品 (`featured: true`)
- ✅ 游标分页 (`after`, `before`)
- ✅ 获取单产品详情 (`post(id)`)
- ✅ 获取主题列表 (`topics`)
- ✅ 获取评论 (`comments`)
- ✅ 获取排名数据 (`dailyRank`, `weeklyRank`, etc.)

### 6.2 不支持的功能
- ❌ 按多个主题筛选（只能传一个 topic）
- ❌ 按投票数范围筛选
- ❌ 关键词搜索产品（无 search 查询）

## 7. 推荐查询策略

### 7.1 每日选品流程
1. **获取当日热门产品**
   ```graphql
   posts(first: 50, order: VOTES, postedAfter: "今天 00:00")
   ```

2. **筛选 SaaS 产品**
   - 方法 A：使用 `topic: "saas"` 直接筛选
   - 方法 B：获取后在客户端根据 topics 过滤

3. **按排名进一步筛选**
   - `dailyRank <= 10` 或 `weeklyRank <= 20`

4. **获取产品详情**
   - 使用 `post(id)` 获取完整信息
   - 提取评论中的用户痛点

### 7.2 推荐的主题筛选
| 主题 | Slug | 适用场景 |
|------|------|----------|
| SaaS | `saas` | 纯 SaaS 产品 |
| Developer Tools | `developer-tools` | 开发者工具 |
| Artificial Intelligence | `artificial-intelligence` | AI 产品 |
| Productivity | `productivity` | 效率工具 |
| Marketing | `marketing` | 营销工具 |
| Sales | `sales` | 销售工具 |
| Design | `design` | 设计工具 |
| E-commerce | `e-commerce` | 电商工具 |

## 8. 注意事项

1. **主题 slug 必须小写连字符**：`"saas"`, `"developer-tools"`，不是 `"SaaS"` 或 `"developer tools"`
2. **日期格式**：ISO 8601 格式，如 `"2026-08-06T00:00:00Z"`
3. **分页游标**：`after` 参数使用 `pageInfo.endCursor`，不是 ID
4. **评论提取**：用于分析用户痛点和需求
5. **排名数据**：`dailyRank` 和 `weeklyRank` 更能反映产品热度

## 9. 数据质量

- ✅ 投票数真实准确
- ✅ 时间戳格式正确
- ✅ 描述内容丰富
- ✅ 话题分类准确
- ✅ 排名数据完整

---

**结论**：API 功能完整，可以通过日期、主题、排名等筛选获取高质量产品数据。
