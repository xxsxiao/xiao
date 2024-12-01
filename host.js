// Script Operator
function operator(proxies, targetPlatform) {
  return proxies.filter(proxy => {
    // 定义免流常见协议集合，包括 trojan 协议
    const freeFlowProtocols = ["ws", "http", "https", "grpc", "trojan"];

    // 标准化协议字段，确保小写格式
    const protocol = proxy["protocol"] ? proxy["protocol"].toLowerCase() : null;

    // 检查协议是否在免流协议集合中
    if (protocol && freeFlowProtocols.includes(protocol)) {
      // 特殊处理 trojan 协议，要求必须有 sni 字段
      if (protocol === "trojan") {
        if (proxy["sni"] && typeof proxy["sni"] === "string" && proxy["sni"].trim() !== "") {
          return true; // 保留包含有效 sni 的 trojan 节点
        }
        return false; // 没有 sni 的 trojan 节点不保留
      }

      // 其他协议直接保留
      return true;
    }

    // 针对部分代理格式没有 "protocol" 字段的特殊处理
    // 通过检查相关配置字段推断协议类型
    if (proxy["ws-opts"] || proxy["http-opts"] || proxy["grpc-opts"]) {
      return true; // 推断为免流相关协议的节点
    }

    // 如果代理缺少协议字段或其他关键配置，则过滤掉
    return false;
  });
}
