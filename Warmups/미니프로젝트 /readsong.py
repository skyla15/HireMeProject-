import os
import string

def song_list_generator(path) -> list and dict:
    print('song gen', path)
    file_names = os.listdir(path)  # 디렉토리 내용 가져옴
    songs = [None] * len(file_names)
    title = [None] * len(file_names)

    for i, file_name in enumerate(file_names):
        f_name = path + file_name
        title_flg = True
        if file_name.endswith('txt'):
            with open(f_name, 'r') as f:
                song = list()       # 잘라라낸 노래들을 담기위한 임시 리스트
                line = None
                while line != '':
                    if title_flg:
                        line = f.readline()
                        title[i] = line.strip(string.punctuation + '/_-() ')
                        title_flg = False
                    line = f.readline()
                    song.extend(line.split())
                    for j in range(len(song)):
                        # song[j].isalnum() : 한글, 알파벳
                        song[j].strip(string.punctuation + '/_-() ')
                        # print(song[j])
                    songs[i] = song

    return title, songs


def swear_list_generator(swear_txt) -> dict:
    swear_dict = dict()
    swear_list = list()   # 임시 리스트
    with open(swear_txt, 'r') as s:
        line = None
        while line != '':
            line = s.readline()
            if line != '\n':
                swear = (line.split(' - '))[0]
            swear_dict[swear] = '😁😁😁😁😁😁'
            swear_list.append(swear)
    return swear_dict


# For문 수정 필요
def compare_word(swear_dict, title_list, song_list):
    print('compare')
    for i in range(len(song_list)):
        print('============== S T A R T ===============')
        print('Censoring : title - {}'.format(title_list[i].strip('\n')))
        print()
        for j in range(len(song_list[i])):
            for k, v in swear_dict.items():
                if song_list[i][j] == k:
                    print('censored : ', song_list[i][j].strip('\n '))
                    song_list[i][j] = v
                    # print('➤➤➤', song_list[i][j])
        print('\n  ∇ Original Song  ∇')
        print(' '.join(song_list[i]))
        print('========== F I N I S H E D ==============')
        print()


def main():
    swearsongs_path = './swearsongs/'
    swear_txt = './swearing/swearings.txt'
    # title_list : 노래 제목 '리스트'
    # song_list : 노래 가사 뛰어쓰기 단위로 분리 된 단어 리스트
    title_list, song_list = song_list_generator(swearsongs_path)
    # swear_dict : k - 욕  / v - ***
    swear_dict = swear_list_generator(swear_txt)
    compare_word(swear_dict, title_list, song_list)


main()


