import pandas as pd
import os
import re


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
    # dir_path = '/home/skylark/PycharmRemote/Vocabulary_Analysis/IELTS词汇_词以类记（完整版）/IELTS词汇_词以类记（完整版）/'
    dir_path = 'D:\Github\Vocabulary_Analysis\IELTS词汇_词以类记（完整版）\IELTS词汇_词以类记（完整版）'
    files = os.listdir(dir_path)
    file_class_dic={}
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'

    for file in files:
        if '意群' in file:
            file_class=file.split('-')[0]
            file_sub_class=file.split('-')[1].split('.')[0]
        else:
            file_class=file.split('：')[0]
            file_sub_class=file.split('：')[1].split('.')[0]
        file_class=re.sub(r1, '', file_class) # 只保留汉字
        if not file_class in file_class_dic:
            file_class_dic[file_class]={}
        if not file_sub_class in file_class_dic[file_class]:
            file_class_dic[file_class][file_sub_class]=[]
        # file_class_dic[file_class].append(os.path.join(dir_path, file))
        file_class_dic[file_class][file_sub_class]=pd.DataFrame(pd.read_csv(os.path.join(dir_path, file), encoding='gb2312').iloc[:,1:])



    print(file_class_dic)
    return file_class_dic



if __name__ == '__main__':
    # corpus = pd.read_csv('./ECDICT/ecdict.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
    # ielts_tag = ielts_sift()
    # vocab_list = vocab_sift(ielts_tag, tag_name='IELTS')


    words_in_class()
    print('OK')
