#! /usr/bin/env python
# -*- coding: utf-8 -*-

from minio import Minio
import sys
from minio.error import ResponseError
from clipboard import get_paste_img_file
from clipboard import alert
from datetime import datetime
import os
import conf


def upload_img():
    try:
        minioClient = Minio(conf.MINIO_URL,
                            access_key=conf.ACCESS_KEY,
                            secret_key=conf.SECRET_KEY)
        
        temp_file = get_paste_img_file()
        if not temp_file:
            alert('您的剪切板里没有图片!')
            sys.exit()
        now = datetime.now()
        upload_img_file = f"{datetime.strftime(now, '%Y%m%d%H%M%S-%f')}.png"
        rrr = minioClient.fput_object('images', upload_img_file, temp_file.name, content_type='image/png')
        mk_url = f"{conf.MARKDOWN_URL_PREFIX}{upload_img_file}"
        os.system("echo '%s' | pbcopy" % mk_url)
        alert("上传成功，已复制url到剪贴板!")
    except ResponseError as err:
        alert(f"程序错误, 请查看{err}")


if __name__ == "__main__":
    upload_img()
