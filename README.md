<div align="center">

# Open WebUI 中文翻译版

**[中文版] Open WebUI — 功能丰富、可扩展的自托管 AI 平台,统一驾驭本地与云端大模型**

[![原项目](https://img.shields.io/badge/原项目-open--webui--open--webui-blue?style=flat-square&logo=github)](https://github.com/open-webui/open-webui)
[![中文文档](https://img.shields.io/badge/中文文档-README.zh--CN.md-orange?style=flat-square)](README.zh-CN.md)
[![GitHub Stars](https://img.shields.io/github/stars/open-webui/open-webui?style=flat-square&label=原项目Stars)](https://github.com/open-webui/open-webui/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 这是 [open-webui/open-webui](https://github.com/open-webui/open-webui) 的中文翻译版本。
> 完整源代码请访问原项目:https://github.com/open-webui/open-webui

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

Open WebUI 是一个可扩展、功能丰富、对用户友好的自托管 AI 平台,官方定位为「AI 之家」。它同时支持 Ollama 与各类 OpenAI 兼容 API,可完全离线运行,为本地模型和云端模型提供统一而强大的使用界面。本仓库是原项目官方 README 的中文翻译版本,帮助中文用户快速了解特性、完成部署与排障。

## ✨ 主要特性

- 🚀 **轻松安装**:支持 pip、uv、Docker、Kubernetes(kubectl / kustomize / helm)等多种方式,并提供 `:ollama`、`:cuda` 标签镜像。
- 🤝 **广泛的模型与 API 集成**:本地 Ollama 模型搭配任意 OpenAI 兼容 API,API 地址可指向 LMStudio、GroqCloud、Mistral、OpenRouter、vLLM 等,自由混搭模型服务商。
- 🔐 **细粒度 RBAC 与用户组**:管理员可定义详细的角色、用户组与权限,默认安全,按组定制体验。
- 🧩 **强大插件体系**:通过 Filters、Actions、Pipes、Tools、Skills 扩展功能,支持 MCP、MCPO 与 OpenAPI 工具服务器接入外部服务,可自定义限流、审批流与数据连接。
- 📚 **本地 RAG 集成**:支持 9 种向量数据库与多种文档抽取引擎,提供 BM25 + 向量混合检索、重排序与全上下文模式,`#` 命令即可引用文档。
- 🔍 **联网搜索 RAG**:接入 SearXNG、Google PSE、Brave、Tavily、Perplexity、DuckDuckGo 等数十家搜索服务商,结果直接注入对话。
- 🎨 **图像生成与编辑**:支持 OpenAI DALL·E、Gemini、ComfyUI、AUTOMATIC1111 等多种引擎。
- 🎤📹 **免提语音/视频通话**:集成 Whisper、Azure、ElevenLabs 等多家语音识别与语音合成引擎。
- 🧠 **持久记忆与多模型对话**:AI 跨对话记住你的偏好;可同时召唤多个模型并行回答、取长补短。
- ⚖️ **生产级部署能力**:Redis 会话与 WebSocket 支持水平扩展,内置 OpenTelemetry 可观测性,支持 LDAP、SSO、SCIM 企业级认证与配置。

## 📁 文件说明

| 文件 | 说明 |
|:-----|:-----|
| README.md | 本文件(中文简介) |
| README.zh-CN.md | 详细中文文档(完整汉化) |

## 🚀 快速开始

**1. 使用 Python pip 安装(需 Python 3.11):**

```bash
pip install open-webui
open-webui serve
```

启动后访问 http://localhost:8080

**2. 使用 Docker 部署(本机已有 Ollama):**

```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

**3. 仅使用 OpenAI API 时:**

```bash
docker run -d -p 3000:8080 -e OPENAI_API_KEY=your_secret_key -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

**4. Open WebUI + Ollama 二合一镜像(CPU 版,GPU 版请看详细中文文档):**

```bash
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

> ⚠️ Docker 部署请务必保留 `-v open-webui:/app/backend/data`,确保数据库正确挂载、防止数据丢失。部署完成后访问 http://localhost:3000

完整源代码与最新版本请访问原项目:https://github.com/open-webui/open-webui

## 📞 联系方式

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [open-webui/open-webui](https://github.com/open-webui/open-webui) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证。

**如果觉得有用,请给原项目点个 Star!** ⭐
