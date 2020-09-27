# -*- coding:utf-8 -*-
import os

import oss2


class OssUtils():
    def __init__(self, access_key_id, access_key_secret, name='tongming1'):
        self.id = access_key_id.strip()
        self.secret = access_key_secret.strip()
        self.name = name

    def make_bucket(self):
        # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
        auth = oss2.Auth(self.id, self.secret)
        # Endpoint以杭州为例，其它Region请按实际情况填写。
        bucket = oss2.Bucket(auth, 'http://oss-cn-chengdu.aliyuncs.com', self.name, connect_timeout=60)
        return bucket

    def upload(self):

        bucket = self.make_bucket()
        # 必须以二进制的方式打开文件，因为需要知道文件包含的字节数。
        # with open('111.png', 'rb') as fileobj:
        # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
        # fileobj.seek(1000, os.SEEK_SET)
        # Tell方法用于返回当前位置。
        # current = fileobj.tell()
        # bucket.put_object('a/b/test.png', fileobj)

        result = bucket.put_object_from_file('111.png', '111.png')
        # HTTP返回码。
        print('http response code: {0}'.format(result.status))
        # 查看本次上传Object的版本id。
        print('put object version:', result.versionid)

    def download(self):
        import shutil
        bucket = self.make_bucket()
        # object_stream是类文件对象，您可以使用shutil.copyfileobj方法，将数据下载到本地文件中。
        object_stream = bucket.get_object('a/b/test.png')
        with open('download.png', 'wb') as local_fileobj:
            shutil.copyfileobj(object_stream, local_fileobj)
        # bucket.get_object_to_file('<yourObjectName>', '<yourLocalFile>')

    def _exist(self):
        bucket = self.make_bucket()

        exist = bucket.object_exists('a/test.png')
        # 返回值为true表示文件存在，false表示文件不存在。
        if exist:
            print('object exist')
        else:
            print('object not exist')

    def file_list(self):
        bucket = self.make_bucket()

        for b in oss2.ObjectIterator(bucket):
            if b.key.endswith("/"):
                print("目录：%s" % b.key)
            else:
                print("文件：%s" % b.key)

    # 管理文件-删除（不占内存，不会彻底删除，有标记）
    def delete_single(self):
        bucket = self.make_bucket()

        # 删除文件。<yourObjectName>表示删除OSS文件时需要指定包含文件后缀在内的完整路径，例如abc/efg/123.jpg。
        # 如需删除文件夹，请将<yourObjectName>设置为对应的文件夹名称。如果文件夹非空，则需要将文件夹下的所有object删除后才能删除该文件夹。
        result = bucket.delete_object('a/b/c/')
        # 查看删除标记。
        print("delete marker: ", result.delete_marker)
        # 查看返回删除标记的版本id。
        print("delete marker versionid: ", result.versionid)

    # 管理文件-删除（不占内存，不会彻底删除，有标记）
    def delete_batch(self):
        bucket = self.make_bucket()

        # 批量删除3个文件。每次最多删除1000个文件。
        result = bucket.batch_delete_objects(['111.png', 'test.png'])
        # 打印成功删除的文件名。
        print('\n'.join(result.deleted_keys))

    def version_delete_single(self, version_id):
        bucket = self.make_bucket()
        object_name = '111.png'

        # 指定object的版本id，也可以是删除标记的版本id。
        params = dict()
        params['versionId'] = version_id

        # 删除指定版本id的object或删除指定删除标记版本id的object。
        result = bucket.delete_object(object_name, params=params)
        print("delete object name: ", object_name)
        # 如果指定的是object的版本id，则返回的delete_marker为None且返回的versionid为前面指定的object版本id。
        # 如果指定的是删除标记的版本id，则返回的delete_marker为True且返回的versionid为前面指定的删除标记的版本id。
        if result.delete_marker:
            print("delete del-marker versionid: ", result.versionid)
        else:
            print("delete object versionid:", result.versionid)

    def get_file_source(self):
        bucket = self.make_bucket()

        # 获取文件的部分元信息
        simplifiedmeta = bucket.get_object_meta("111.png")
        print(simplifiedmeta.headers['Last-Modified'])
        print(simplifiedmeta.headers['Content-Length'])
        print(simplifiedmeta.headers['ETag'])

        # 获取文件的全部元信息
        objectmeta = bucket.head_object("111.png")
        print(objectmeta.headers['Content-Type'])
        print(objectmeta.headers['Last-Modified'])
        print(objectmeta.headers['x-oss-object-type'])


if __name__ == '__main__':
    oss = OssUtils()
    oss.version_delete_single('')