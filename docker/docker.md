docker学习文档

1:在dockerfile文件路径下，执行打包成自定义镜像
    docker build -t myimage:latest .

2:把自定义镜像打包成tar包
    docker save myimage:latest -o myimage.tar

3:创建并启动一个新的Docker自定义容器
    docker run -it myimage:latest /bin/bash    

4:启动容器
    docker start 87be4bca2646

5:进入容器的交互式页面
    docker exec -it 87be4bca2646 /bin/bash    