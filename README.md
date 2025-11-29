# Port-Scanner
一个用python编写的多线程端口扫描器，用于网络安全学习和实践

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 功能特性

- **多线程扫描**：使用Python的threading库，大幅提升扫描效率
- **常用端口扫描**：内置常见服务端口列表，快速识别开放服务
- **TCP连接检测**：基于TCP全连接扫描，结果准确可靠
- **简单易用**：只需运行一个Python文件即可开始扫描

## 🛠️ 安装与使用

### 环境要求
- Python 3.6+
- 无需额外依赖库
### 使用方法
1. 克隆项目到本地
 ```bash
git clone https://github.com/Qian4952/Port-Scanner.git
cd Port-Scanner
```
2. 运行以下命令：
```bash
python scanner.py
```
3. 根据提示输入目标IP地址（如 127.0.0.1 测试本机）和线程数量
程序将自动扫描预定义的常用端口列表

## 高级使用

如需扫描特定端口范围，可修改代码中的 port_list 变量：

```python
# 在端口扫描.py中修改这一行
port_list = [80, 443, 21, 22, 23, 25, 53, 110, 135, 139, 143, 445, 993, 995]
```
📸 运行演示

扫描本地主机的结果示例：

```
[*] 开始扫描，请稍候...
[+] 端口 25/tcp 是 **开放的**
[+] 端口 143/tcp 是 **开放的**

[+] 端口 110/tcp 是 **开放的**


[*] 扫描结束！
```
📁 项目结构

```
Port-Scanner/
├── 端口扫描.py          # 端口扫描器主程序
├── README.md          # 项目说明文档
└── LICENSE            # MIT许可证文件
```

🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

📄 许可证

本项目基于 MIT License 开源。

⚠️ 免责声明

本项目仅用于网络安全学习和授权测试，请勿用于非法用途。
