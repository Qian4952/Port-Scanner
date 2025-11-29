import socket
import threading
from queue import Queue

print("端口扫描器 (启动！)")

# 1. 获取目标
target = input("请输入要扫描的目标主机 (IP或域名): ")


# 可以扫描的常用端口列表
port_list = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]

# 2. 创建一个队列，放入所有要扫描的端口
queue = Queue()
for port in port_list:
    queue.put(port)

# 3. 定义扫描一个端口的函数
def scan_port(port):
    try:
        # 创建socket对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间，避免长时间等待
        sock.settimeout(1)
        # 尝试连接目标主机的指定端口
        result = sock.connect_ex((target, port))
        if result == 0:
            # 连接成功，端口开放！
            print(f"[+] 端口 {port}/tcp 是 **开放的**\n")
        # 关闭socket连接
        sock.close()
    except Exception as e:
        # 如果出错，简单跳过
        pass

# 4. 定义工作线程函数
def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)

# 5. 创建并启动多个线程
thread_list = []
# 设置线程数量，可以根据情况调整
thread_count = int(input("输入线程数量"))
print("[*] 开始扫描，请稍候...")
for t in range(thread_count):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    thread.start()

# 6. 等待所有线程完成
for thread in thread_list:
    thread.join()

print("[*] 扫描结束！")
