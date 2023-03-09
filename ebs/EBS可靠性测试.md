EBS可靠性测试

1:容器故障
    1:kubectl get pods -n bytedrive
    2:kubectl delete pod bdcjy1qrcwybxl6hozi5pej-n56-113-024-blockserver-0 -n bytedrive

2:进程故障
    1:kubectl get pods -n bytedrive
    2:kubectl exec -it bdcjy1qrcwybxl6hozi5pej-n56-113-024-blockserver-0 /bin/bash -n bytedrive
    3:ps -ef
    4:kill -9 41

3:节点故障
    1:echo 'c' > /proc/sysrq-trigger
    2:uptime  查看是否重启