> 🌐 本文档由 [open-webui/open-webui](https://github.com/open-webui/open-webui) 翻译,英文原版见原项目。

# Open WebUI 故障排除指南

## 理解 Open WebUI 的架构

Open WebUI 的系统设计目标是精简客户端(你的浏览器)与 Ollama API 之间的交互。这套设计的核心是一个后端反向代理,用于增强安全性并解决 CORS 问题。

- **工作原理**:Open WebUI 被设计为通过一条特定的路由与 Ollama API 交互。当 WebUI 向 Ollama 发起请求时,请求并不会直接发送到 Ollama API。请求首先会通过 `/ollama` 路由发送到 Open WebUI 后端,再由后端负责把请求转发给 Ollama API。转发所使用的地址由 `OLLAMA_BASE_URL` 环境变量指定。因此,在 WebUI 中对 `/ollama` 发起的请求,实际上等价于在后端对 `OLLAMA_BASE_URL` 发起的请求。例如,WebUI 中的 `/ollama/api/tags` 请求等价于后端的 `OLLAMA_BASE_URL/api/tags`。

- **安全收益**:这种设计避免了把 Ollama API 直接暴露给前端,可以防范潜在的 CORS(跨域资源共享)问题和未授权访问。要求通过身份验证才能访问 Ollama API,进一步强化了这一安全层。

## Open WebUI:服务器连接错误

如果你遇到连接问题,通常是因为 WebUI 的 Docker 容器无法访问容器内的 Ollama 服务器 127.0.0.1:11434(host.docker.internal:11434)。在 docker 命令中使用 `--network=host` 参数即可解决。注意此时端口会从 3000 变为 8080,访问链接变为:`http://localhost:8080`。

**Docker 命令示例**:

```bash
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### Ollama 响应缓慢导致的错误

Open WebUI 默认给 Ollama 5 分钟的超时时间来完成响应生成。如有需要,可以通过环境变量 AIOHTTP_CLIENT_TIMEOUT 调整,该变量以秒为单位设置超时时间。

### 一般性连接错误

**确保 Ollama 版本为最新**:排查的第一步永远是确认你的 Ollama 是最新版本。请访问 [Ollama 官网](https://ollama.com/) 获取最新更新。

**故障排除步骤**:

1. **核对 Ollama URL 格式**:
   - 运行 Web UI 容器时,确保 `OLLAMA_BASE_URL` 设置正确(例如跨主机部署时可设为 `http://192.168.1.1:11434`)。
   - 在 Open WebUI 中,进入"设置" > "常规"。
   - 确认 Ollama 服务器 URL 已正确设置为 `[OLLAMA URL]`(例如 `http://localhost:11434`)。

按照以上增强版故障排除步骤操作后,连接问题应能得到有效解决。如需进一步帮助或有疑问,欢迎随时在我们的社区 Discord 上联系我们。
