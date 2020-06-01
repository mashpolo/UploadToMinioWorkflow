from minio import Minio
from minio.error import ResponseError
import urllib3
import os
from test_clipboard import get_paste_img_file
from datetime import datetime


minioClient = Minio('image.mashpolo.com',
                    access_key='admin_hd_luluo',
                    secret_key='admin_hd_101217')


buckets = minioClient.list_buckets()


temp_file = get_paste_img_file()
now = datetime.now()
upload_img_file = f"{datetime.strftime(now, '%Y%m%d%H%M%S-%f')}.png"

print(f"this file is {temp_file}")

try:
    minioClient.fput_object('images', upload_img_file, temp_file, content_type='image/png')
    hello = f"https://image.mashpolo.com/images/{upload_img_file}"
    print(hello)
except ResponseError as err:
    print(err)
