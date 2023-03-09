redis常稳工具使用

1: 安装工具
    redis-5.0.41

    scp -r /Users/bytedance/Downloads/redis-6.0.9 root@10.56.239.46:/root/redis-6.0.9
    mv redis-6.0.9 /usr/local/redis
    cd /usr/local/redis
    make
    make install

2: redis常稳工具使用
    cd /usr/local/redis/src
    redis-server & #后台启动redis   

    脚本：
    #!/bin/bash
    while true
    do
    echo `date` 'start redis-benchmark'
    redis-benchmark -h 10.56.239.116 -p 6379 -c 50 -n 10000 -t set,lpush -l
    echo `date` 'finish redis-benchmark'
    sleep 1s
    done

    nohup sh redis.sh > test.log &
    grep -i "redis-benchmark" test.log #查询关键字 看故障
