### 修改linux最大连接数
##### 第一步:修改系统文件限制

```bash
#  vim /etc/security/limits.conf
# 用户 类型(软限制、硬限制) nofile 数量
# 所有用户限制数量1024*1024*2，百万连接数
* soft nofile 1048576
* hard nofile 1048576

# 如果默认值小于1048576，修改系统最大文件数量,
echo 1048576 > /proc/sys/fs/file-max
# 如果默认值小于1048576，修改系统最大打开文件数量
echo 1048576 > /proc/sys/fs/nr_open

# 检查session配置
vim /etc/pam.d/common-session
# 开启以下配置
session required pam_limits.so
```

##### 第二步:修改网络IO配置

```bash
# vim /etc/sysctl.conf
# 临时随机端口范围，两个字节，最大65535
net.ipv4.ip_local_port_range = 1024 65535
# 最大半连接数(握手尚未完成)
net.ipv4.tcp_max_syn_backlog = 1048576
# 最大连接数(握手完成)
net.core.somaxconn = 1048576
# 读取内存配置，最小、限制、最大，单位页(默认4KB)
net.ipv4.tcp_rmem = 4096 87380 8388608
# 连接内存配置，最小、限制、最大，单位页(默认4KB)
net.ipv4.tcp_mem = 4096 87380 8388608
# 写入内存配置，最小、限制、最大，单位页(默认4KB)
net.ipv4.tcp_wmem = 4096 87380 8388608
# 等待状态连接是否回收用于新的TCP连接
net.ipv4.tcp_tw_reuse = 1
# 新建连接握手失败重试次数
net.ipv4.tcp_syn_retries = 2
# 近端丢弃TCP连接之前重试次数
net.ipv4.tcp_orphan_retries = 2
# 允许孤儿TCP数，超出则回收
net.ipv4.tcp_max_orphans = 2000
# 连接哈希表长度
nf_conntrack_max = 314572800

# 生效配置
sysctl -p 
```
