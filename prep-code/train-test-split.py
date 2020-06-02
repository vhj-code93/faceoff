import os
import random
import boto3
import time

f1 = open('s3_touch.txt','r')
f2 = open('s3_no-touch.txt','r')

touch_files = []
no_touch_files = []

lines1 = f1.readlines()
lines2 = f2.readlines()

for i in lines1:
    touch_files.append(i.split(' ')[7].strip())

for j in lines2:
    no_touch_files.append(j.split(' ')[7].strip())

random.shuffle(touch_files)

random.shuffle(no_touch_files)

s3 = boto3.resource('s3')

#assuming train:test split of 70:30
train_samples_touch = int(0.7*len(touch_files))
#test_samples_touch = len(touch_files) - train_samples_touch

train_samples_no_touch = int(0.7*len(no_touch_files))
#test_samples_no_touch = len(no_touch_files) - train_samples_no_touch

for i in range(0,len(touch_files)):
    copy_source = {
        'Bucket': 'ml-repo',
        'Key': 'faceoff-extended/touch/'+touch_files[i]
    }
    if i<train_samples_touch:
        target_key = 'faceoff-extended/train/touch/'+touch_files[i]
    else:
        target_key = 'faceoff-extended/test/touch/'+touch_files[i]
    s3.meta.client.copy(copy_source, 'ml-repo', target_key)
    time.sleep(.500)

for i in range(0,len(no_touch_files)):
    copy_source = {
        'Bucket': 'ml-repo',
        'Key': 'faceoff-extended/no-touch/'+no_touch_files[i]
    }
    if i<train_samples_no_touch:
        target_key = 'faceoff-extended/train/no-touch/'+no_touch_files[i]
    else:
        target_key = 'faceoff-extended/test/no-touch/'+no_touch_files[i]
    s3.meta.client.copy(copy_source, 'ml-repo', target_key)
    time.sleep(.500)

