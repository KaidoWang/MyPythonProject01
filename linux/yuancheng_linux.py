import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到远程主机
ssh.connect('192.168.0.100', username='user', password='password')

# 执行命令并打印输出
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())

# 关闭连接
ssh.close()
