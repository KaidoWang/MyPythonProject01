常见的故障注入方法
主机故障
- 重启 reboot
- 重启 reboot -f
- 立即重启 echo 'b' > /proc/sysrq-trigger
- 【推荐】crash重启 echo 'c' > /proc/sysrq-trigger


网络故障
网络故障注入会导致设备无法连接，从而故障无法恢复。网络故障注入需要通过编写脚本后台运行故障和恢复故障命令。
- tc模拟网络故障
  - 网络时延 tc qdisc add dev bond0 root netem delay 300ms
  - 网络丢包 tc qdisc add dev bond0 root netem loss 7%
  - 重复包 tc qdisc add dev bond0 root netem duplicate 1%
  - 取消网络故障注入  tc qdisc del dev bond0 root netem
- ifconfig模拟网络故障
  - 网络故障注入 Ifconfig bond0 down
  - 网络故障恢复 Ifconfig bond0 up;systemctl restart networking.service
  物理机环境可以直接使用此脚本，上传到要进行故障的节点给脚本添加权限执行即可
chmod +x neterror.sh
nohup ./neterror.sh &
  neterror.sh
- ifdown模拟网络故障
  - 网络故障注入 ifdown bond0
  - 网络故障恢复 ifup bond0


磁盘故障
普通盘模拟拔插
1、ls -l /sys/block/      //查看磁盘的盘符id
2、echo 1 > /sys/bus/pci/devices/0000\:42\:00.0/remove    //针对nvme
3、echo 1 > /sys/block/sdc/device/delete   //针对hdd
4、ls /sys/class/scsi_host/         //恢复磁盘
host0  host1  host2
# echo '- - -'  > /sys/class/scsi_host/host0/scan
# echo '- - -'  > /sys/class/scsi_host/host1/scan
# echo '- - -'  > /sys/class/scsi_host/host2/scan

被spdk接管后，nvme盘符就无法lsblk看到了，只能看pci号
此时需要使用工具模拟故障磁盘，参考：SPDK故障模拟工具使用方法 
1、找到要故障节点上的chunkserver进入 kubectl exec -it bytestore-12-26-15002-bs-ebs-chunkserver-0 -nbytestore bash
2、在pod里面查看要故障的磁盘cat /opt/tiger/spdk.conf
3、执行脚本./rpc.py bdev_set_failure_inject -b Nvme2n1 -e
4、恢复故障./rpc.py bdev_set_failure_inject -b Nvme2n1 -d
5、重启对应的chunkserver
6、查看磁盘io情况./iostat.py  -i 1 -t 1000


容器故障
容器故障直接删除pod：kubectl delete pod $podname -n$ns


进程故障
杀进程：kill -9 $pid
挂起进程：kill -19 $pid
恢复挂起的进程：kill -18 $pid


资源故障
常用工具：chaosblade，可自行下载https://github.com/chaosblade-io/chaosblade
内存占用：./blade create mem load --mem-percent 95 --mode ram
cpu占用：./blade create cpu load --cpu-percent 85
恢复故障：./blade destroy  xxxx
磁盘io占用：使用fio工具直接使用direct io读写文件占用磁盘io
网络io占用：使用iperf、netpef打压