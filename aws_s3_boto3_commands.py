import boto3

# create s3 client 
s3_client = boto3.client('s3', region_name='us-east-1', aws_access_key_id='', aws_secret_access_key='')

# list buckets, cli command: aws s3 ls
buckets = s3_client.list_buckets()
for bucket in buckets['Buckets']:
    print(bucket)

# get all objects of bucket,cli command: aws s3 ls s3://butterfly-bucket/
resp = s3_client.list_objects(Bucket='butterfly-bucket')

# get object details, cli command: aws s3 ls s3://bucket-name/object-name.txt
obj_resp = s3_client.head_object(Bucket='butterfly-bucket', Key='paper.jpg')

'''
upload a file/folders to bucket:
  aws cli command: aws s3 cp sourcePath destinationPath
                   aws s3 cp --recursive sourcePath sourcePath  
                  NOTE : for copying all the objects of particular folder to destination "aws s3 cp --recursive source destination" 

   source: source location absolute path/relative
   destination: any bucket or folder in s3

   we can upload or copy ojects from source to destination using upload_file in boto3
'''
s3_client.upload_file(Filename=r'C:\Users\DeLL\Desktop\aws_reference.txt', Bucket='butterfly-bucket', Key='test_folder/aws_reference.txt')
s3_client.upload_file(Filename=r'C:\Users\DeLL\Desktop\steps_django_project\steps_django_project.py', Bucket='butterfly-bucket', Key='django_set-up_folder/steps_django_project.py')
s3_client.upload_file(Filename=r'C:\Users\DeLL\Desktop\impl_dfs_stack.py', Bucket='butterfly-bucket', Key='Stack/impl_dfs_stack.py')

# download a file
file = s3_client.download_file(Filename=r'C:\Users\DeLL\Desktop\impl_dfs_stack_2.py',Bucket='butterfly-bucket',Key='Stack/impl_dfs_stack.py')

# delete all the objects of bucket, cli command: aws s3 rm s3://mybucket --recursive
# NOTE:  you can't delete bucket directly
resp = s3_client.delete_bucket(Bucket='git-request')

resp = s3_client.list_objects(Bucket='git-request')
for obj_dict in resp['Contents']:
    print('Deleting', obj_dict['Key'])
    s3_client.delete_object(Bucket='git-request', Key=obj_dict['Key'])

# delete bucket
resp = s3_client.delete_bucket('git-request')


