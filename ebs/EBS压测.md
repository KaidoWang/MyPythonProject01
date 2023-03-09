EBS压测

1:准备工作
    所需工具：
        1:scp -r /Users/bytedance/Downloads/jdk-8u341-linux-x64.tar.gz relay@10.22.253.235:/home/relay/jdk-8u341-linux-x64.tar.gz
        2:scp -r /Users/bytedance/Downloads/vdbench50406 relay@10.22.253.235:/home/relay/vdbench50406
        3:根据文档安装java: https://blog.csdn.net/wcy1900353090/article/details/125121855

    配置文件:
        #单磁盘 1m 1深度 1线程 顺序写
        messagescan=no
        sd=default,thread=1,openflags=o_direct,size=50G
        sd=sd1,lun=/dev/vdb
        wd=wd1,sd=sd*,xfersize=1m,rdpct=0,seekpct=0
        rd=rd1,wd=wd1,iorate=max,el=3600,warmup=10

2:执行脚本
    #具体执行命令
    #!/bin/zsh
    for i in $( seq 1 54)
    do
    ./vdbench -f  ebs_xingneng_peizhi/$i.txt -o output/00$i 
    done

    nohup sh ebs_io.sh >test.log&

