EBS可靠性测试

1:容器故障

    1:kubectl get pods -n bytedrive
    2:kubectl delete pod bdcjy1qrcwybxl6hozi5pej-n56-113-024-blockserver-0 -n bytedrive

![image](https://github.com/KaidoWang/MyPythonProject01/blob/master/images/ebs1.png)
2:进程故障

    1:kubectl get pods -n bytedrive
    2:kubectl exec -it bdcjy1qrcwybxl6hozi5pej-n56-113-024-blockserver-0 /bin/bash -n bytedrive
    3:ps -ef
    4:kill -9 41
![image](https://github.com/KaidoWang/MyPythonProject01/blob/master/images/ebs2.png)

3:节点故障

    1:echo 'c' > /proc/sysrq-trigger
    2:uptime  查看是否重启
![image](https://github.com/KaidoWang/MyPythonProject01/blob/master/images/ebs3.png)    