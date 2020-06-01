# 利用alfred workflow上传图片到minio

> minio是aws开源的一个类似s3的存储程序，可以用来当作图床

## 搭建minio

```bash
docker pull minio/minio
docker run -p 9000:9000 minio/minio server /data
```

## 生成配置文件

1. 需要往conf.py中填入必备的参数，否则无法使用
2. 将文件拷贝入自己创建的空白workflow目录
