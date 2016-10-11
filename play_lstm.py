import chainer.links as L
import chainer.serializers as S
import pickle
import nico_lstm
import unicodedata
import numpy as np
import six


with open('./sample_vocab.pkl', 'rb') as f:
    vocab = pickle.load(f)
    vocab += ['<soc>', '<eoc>']  # start of comment, end of comment
    index2vocab = {i: word for i, word in enumerate(vocab)}
    vocab2index = {word: i for i, word in enumerate(vocab)}
with open('./sample_texts.pkl', 'rb') as f:
    texts = pickle.load(f)
    train = []
    for text in texts:
        train.append(vocab2index['<soc>'])
        for i in text:
            train.append(vocab2index[i])
        train.append(vocab2index['<eoc>'])

n_vocab = max(train) + 1  # train is just an array of integers
print('#vocab =', n_vocab)
n_train = len(train)  # train is just an array of integers
print('#train =', n_train)

rnn = nico_lstm.RNNForLM(n_vocab, 650)
model = L.Classifier(rnn)
S.load_npz('./result/lstm_model.npz', model)


def make_comment(word):
    try:
        com = unicodedata.normalize('NFKC', word)
    except:
        return '{} is not in vocab'.format(word)

    rnn.reset_state()
    init = rnn(np.asarray([vocab2index['<soc>']], dtype=np.int32))
    comment = ''
    for i in list(com):
        a = rnn(np.asarray([vocab2index[i]], dtype=np.int32))
        comment += i

    while True:
        now = index2vocab[int(np.argmax(a.data))]
        if now == '<eoc>':
            break
        elif len(comment) > 20:
            break
        comment += now
        a = rnn(np.asarray([vocab2index[now]], dtype=np.int32))

    return comment

try:
    while True:
        q = six.moves.input('>> ')
        print(make_comment(q))

except EOFError:
    pass