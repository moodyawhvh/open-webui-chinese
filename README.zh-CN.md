<div align="center">

# Open WebUI 中文文档

[![原项目](https://img.shields.io/badge/原项目-open--webui--open--webui-blue?style=flat-square&logo=github)](https://github.com/open-webui/open-webui)
[![GitHub Stars](https://img.shields.io/github/stars/open-webui/open-webui?style=flat-square&label=原项目Stars)](https://github.com/open-webui/open-webui/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

> 本文档是 [open-webui/open-webui](https://github.com/open-webui/open-webui) 官方 README 的中文翻译,仅供学习参考;如有出入请以英文原文与官方文档为准。

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

Open WebUI 是「AI 之家」:一个可扩展、功能丰富、对用户友好、可完全离线运行的**自托管 AI 平台**。它支持 **Ollama** 与 **OpenAI 兼容 API**,为本地与云端模型提供强大且不绑定单一厂商的统一界面。

更多详细信息请查阅官方文档(https://docs.openwebui.com/)。

## ✨ 主要特性 ⭐

- 🚀 **轻松安装**:可通过 pip、uv、Docker 或 Kubernetes(kubectl、kustomize 或 helm)无缝安装,容器部署提供 `:ollama` 与 `:cuda` 标签镜像。
- 🤝 **广泛的模型与 API 集成**:本地 Ollama 模型之外,可接入任何 OpenAI 兼容 API,API 地址可指向 LMStudio、GroqCloud、Mistral、OpenRouter、vLLM 等服务,自由混搭模型供应商。
- 🔐 **细粒度 RBAC 与用户组**:管理员可定义精细的角色、用户组与权限,让每位用户恰好获得所需访问权;默认安全,并按组定制体验。
- 🧩 **插件支持**:通过 Filters(过滤器)、Actions(动作)、Pipes(管道)、Tools(工具)与 Skills(技能)扩展功能;经由 MCP、MCPO 与 OpenAPI 工具服务器连接外部服务,可构建自定义集成、限流、审批流与数据连接。
- 🤖 **模型与智能体**:用自定义指令、工具和知识包装任意基座模型,构建专属智能体;支持动态变量、按用户/用户组的访问控制,并可从 Open WebUI Community 导入社区预设。
- 📝 **笔记**:专用于对话之外内容的工作区;富文本编辑器起草、AI 改写选中文本,笔记可附加到任意聊天实现全上下文注入。
- 📢 **频道**:实时共享空间,团队与 AI 模型在同一条时间线上协作;@模型起草或点评,支持话题串、表情、置顶与访问控制。
- 🧠 **持久记忆**:AI 跨对话记住关于你的事实,上下文在不同聊天之间延续。
- ✅ **实时工作流与消息流**:实时观看 AI 构建并执行清单;AI 尚在回复时也可排队消息,就绪后自动发送。
- 📅 **日历与 AI 日程 / 自动化**:内置个人与共享日历(月/周/日视图、循环事件、提醒),模型通过原生函数调用对话式管理日程;提示词可按周期定时执行,运行记录呈现在日历上。
- 📱 **响应式设计与 PWA**:桌面、笔记本、手机无缝切换,渐进式 Web 应用带来原生应用般的体验。
- ✒️🔢 **完整 Markdown 与 LaTeX 支持**:为深度交互提供全面的排版与公式能力。
- 🎤📹 **免提语音/视频通话**:集成多家语音转文字服务(本地 Whisper、OpenAI、Deepgram、Azure)与文字转语音引擎(Azure、ElevenLabs、OpenAI、Transformers、WebAPI)。
- 💾 **持久化工件存储**:内置键值存储 API,支撑日志、追踪器、排行榜与协作工具,数据分个人与共享两种作用域。
- 📚 **本地 RAG 集成**:检索增强生成由 9 种向量数据库与多种内容抽取引擎(Tika、Docling、Document Intelligence、Mistral OCR、PaddleOCR-vl 等)支撑;支持混合检索(BM25 + 向量)、重排序与全上下文模式;可加载文档进聊天,或用 `#` 命令从资料库引用。
- 🔍 **RAG 联网搜索**:通过 SearXNG、Google PSE、Brave、Kagi、Tavily、Perplexity、DuckDuckGo、Bing、Jina、Exa、搜狗、Azure AI Search 等数十家服务商搜索网络,结果直接注入对话。
- 🌐 **网页浏览能力**:聊天中用 `#` 命令加 URL 抓取网页,也可让模型在需要时自行获取。
- 🎨 **图像生成与编辑**:使用 OpenAI DALL·E、Gemini、ComfyUI(本地)、AUTOMATIC1111(本地)等引擎,支持生成与基于提示词的编辑。
- ⚙️ **多模型对话**:同时与多个模型对话,并行发挥各自长处,获得最佳回答。
- 📊 **用量分析与模型评估**:管理仪表盘按用户与模型统计消息量、Token 消耗与成本;内置竞技场、A/B 测试与 ELO 排行榜评估模型。
- 🗄️ **灵活的数据库与存储**:可选 SQLite(可加密)或 PostgreSQL;文件可存本地或 S3、Google Cloud Storage、Azure Blob Storage。
- 🪪 **企业级认证与开通**:完整 LDAP/Active Directory 集成、可信请求头与 OAuth SSO,以及面向 Okta、Azure AD、Google Workspace 等身份源的 SCIM 2.0 自动开通;另有 Google Drive 与 OneDrive/SharePoint 原生文件选择器。
- 🔭 **生产可观测与水平扩展**:内置 OpenTelemetry 输出追踪、指标与日志;基于 Redis 的会话管理与 WebSocket 支持,适配负载均衡后的多 worker、多节点部署。
- 🌍 **多语言支持**:i18n 国际化,可切换界面语言(含中文)。
- 🛡️ **透明的安全流程**:安全报告经分类、修复并以公开通告形式发布,遵循文档化的负责任披露流程。

## 🌐 Open WebUI 生态

Open WebUI 是核心,周边配套应用与基础设施进一步扩展 AI 的能力与运行方式:

- 💻 **Open WebUI Computer**:独立、移动优先的电脑与编程智能体,运行在你自己的机器上;浏览器标签页集文件、终端与 git,手机可随时访问;可作为模型接入 Open WebUI,或经 Telegram、WhatsApp 联系。
- ⚡ **Open Terminal 与 Terminals(企业版)**:接入 Open WebUI 的自托管算力环境,让 AI 在聊天内写代码、执行、读输出、修错并迭代;企业版提供按用户隔离的容器、独立凭据、资源限额与网络规则。
- 🔄 **oikb**:从 45+ 来源(GitHub、Confluence、ServiceNow、Salesforce、Jira、Slack、SharePoint、Notion 等)持续同步,喂养你的知识库。
- 🖥️ **原生桌面应用**:在 macOS、Windows、Linux 上以原生应用运行;系统级 Spotlight 风格聊天条、截图、按住说话,可选用内置 llama.cpp 引擎完全本地推理。

## 🚀 如何安装

### 通过 Python pip 安装 🐍

使用 pip 安装 Open WebUI。开始前请确保使用 **Python 3.11**,以避免兼容性问题。

1. **安装 Open WebUI**,在终端执行:

   ```bash
   pip install open-webui
   ```

2. **运行 Open WebUI**,安装完成后执行:

   ```bash
   open-webui serve
   ```

服务将在 http://localhost:8080 启动,浏览器打开即可使用。

### Docker 快速开始 🐳

> [!WARNING]
> 使用 Docker 安装时,请务必在命令中带上 `-v open-webui:/app/backend/data`,确保数据库正确挂载、防止数据丢失。

> [!TIP]
> 如需 Open WebUI 与 Ollama 捆绑或 CUDA 加速,建议使用 `:cuda` 或 `:ollama` 标签的官方镜像;启用 CUDA 需在 Linux/WSL 上安装 Nvidia CUDA 容器工具包。

**默认配置安装(Ollama 在本机):**

```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

**Ollama 在另一台服务器**,把 `OLLAMA_BASE_URL` 改为对应地址:

```bash
docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=https://example.com -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

**Nvidia GPU 支持:**

```bash
docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
```

**仅使用 OpenAI API:**

```bash
docker run -d -p 3000:8080 -e OPENAI_API_KEY=your_secret_key -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

**捆绑 Ollama 的一体化镜像**(单容器同时运行 Open WebUI 与 Ollama,GPU 版把 `-v ollama:/root/.ollama` 前加 `--gpus=all`):

```bash
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

安装完成后访问 http://localhost:3000 即可使用。

**其他安装方式:** 官方还提供非 Docker 原生安装、Docker Compose、Kustomize 与 Helm 等,详见官方文档入门章节。

**故障排查(服务器连接错误):** 若容器无法访问本机 127.0.0.1:11434 的 Ollama,可在 docker 命令中使用 `--network=host`(此时端口由 3000 变为 8080):

```bash
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

**使用 dev 分支 🌙:** `:dev` 标签包含最新不稳定特性,可能存在 bug,请自行评估风险;命令同上,把镜像标签换成 `:dev` 即可。

### 离线模式

在离线环境中运行时,可设置环境变量 `HF_HUB_OFFLINE=1`,阻止联网下载模型:

```bash
export HF_HUB_OFFLINE=1
```

## 📜 许可证

本项目包含多许可证代码:当前代码库包含遵循 Open WebUI License(附加保留 "Open WebUI" 品牌要求)的组件,以及按各自原始许可证授权的历史贡献。许可变更与各部分适用条款详见仓库内 LICENSE_HISTORY 与 LICENSE 文件。

## 💬 支持

如有疑问、建议或需要帮助,请到原仓库提交 issue,或加入 Open WebUI Discord 社区(https://discord.gg/5rJgQTnV4s)。

## 🛡️ 安全

如发现安全漏洞,请通过 GitHub 上的负责任披露程序私密报告;官方仅接受通过 GitHub 提交的安全报告。

## 🔗 相关链接

- 官方文档:https://docs.openwebui.com/
- 社区站点:https://openwebui.com/
- 路线图:https://docs.openwebui.com/roadmap/
- 安全策略:https://github.com/open-webui/open-webui/security

---

> 本文档为 [open-webui/open-webui](https://github.com/open-webui/open-webui) 官方 README 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证。

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

**如果觉得有用,请给原项目点个 Star!** ⭐
