import jsonlines
import os
import boto3

'''
{"source-ref":"s3://image/filename1.jpg", "class":"0"}
0 -> no-touch
1 -> touch
'''

#start off with train data
with jsonlines.open('faceoff-train.manifest', mode='w') as writer:
    f = open ('train-no_touch.txt','r')
    for i in f.readlines():
        text = {"source-ref": "s3://ml-repo/faceoff-extended/train/no-touch/"+i.split(' ')[7].strip(), "class":"0"}
        writer.write(text)
    f.close()
    f = open('train-touch.txt','r')
    for i in f.readlines():
        text = {"source-ref": "s3://ml-repo/faceoff-extended/train/touch/"+i.split(' ')[7].strip(), "class":"1"}
        writer.write(text)
    f.close()



#then with test data
with jsonlines.open('faceoff-test.manifest', mode='w') as writer:
    f = open ('test-no_touch.txt','r')
    for i in f.readlines():
        text = {"source-ref": "s3://ml-repo/faceoff-extended/test/no-touch/"+i.split(' ')[7].strip(), "class":"0"}
        writer.write(text)
    f.close()
    f = open('test-touch.txt','r')
    for i in f.readlines():
        text = {"source-ref": "s3://ml-repo/faceoff-extended/test/touch/"+i.split(' ')[7].strip(), "class":"1"}
        writer.write(text)
    f.close()

