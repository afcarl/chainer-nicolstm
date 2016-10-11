# chainer-nicolstm

## Requirements
- Python 2.7 or 3.4
- Chainer 1.16.0

## Usage
### Step1
Downloads data from NII.   
ニコニコ動画コメント等データ([http://www.nii.ac.jp/dsc/idr/nico/nicocomm-apply.html](http://www.nii.ac.jp/dsc/idr/nico/nicocomm-apply.html))

### Step2
Get latest 10 comments from each nico-douga.   
It outputs 'last10comments.pkl'.
```
$ python maesyori1.py /path/to/data/thread/
```

### Step3
Get sample comments that were selected randomly.   
It outputs 'sample_texts.pkl' and 'sample_vocab.pkl'.
```
$ python maesyori2.py
```

### Step4
Train comment-data by lstm.   
It outputs '/result/lstm_model.npz'.
```
$ python nico_lstm.py -g <gpu_id
```
### Step5
Play generating comment.   
Input bag of comment.
```
$ python play_lstm.py
>> ┗(^
┗(^o^ )┓三
>> 日本語
日本語でおk
>> 
````
