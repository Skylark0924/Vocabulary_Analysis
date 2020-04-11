import pandas as pd
import os


def ielts_sift():
    tag_dict = {}
    ielts = []
    tag_dict = pd.value_counts(corpus['tag'])
    for key, _ in tag_dict.items():
        if 'ielts' in key:
            ielts.append(key)
    print(ielts)
    return ielts


def vocab_sift(tag_list, tag_name):
    vocab = []
    for i in range(len(corpus['tag'])):
        if corpus['tag'][i] in tag_list:
            vocab.append([])
            vocab[len(vocab) - 1] = corpus.iloc[i, 1:]

    vocab = pd.DataFrame(vocab)
    print('{}: {}'.format(tag_name, len(vocab)))
    vocab.to_csv('./ECDICT/{}.csv'.format(tag_name))
    return vocab


def words_in_class():
    dir_path = '/home/skylark/PycharmRemote/Vocabulary_Analysis/IELTS词汇_词以类记（完整版）/IELTS词汇_词以类记（完整版）/'
    files = os.listdir(dir_path)
    for file in files:
        print(file)


if __name__ == '__main__':
    # corpus = pd.read_csv('./ECDICT/ecdict.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
    # ielts_tag = ielts_sift()
    # vocab_list = vocab_sift(ielts_tag, tag_name='IELTS')


    words_in_class()
    print('OK')
