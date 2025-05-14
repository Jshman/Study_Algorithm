# 비트코인 채굴하기
alphabets = [chr(i) for i in range(97,123)]
alphabets.append('')

def hashing(string):
    n = len(string)
    ret = 0
    for i in range(n):
        ret = (ret + (ord(string[i])-96)*(31**i))%1234567891
    return ret

def count_number_of_ONE(hsh):
    cnt = 0
    for i in range(len(hsh)):
        if hsh[i] == '1':
            cnt+=1
            continue
        break
    return cnt

if __name__=='__main__':

    string = ['','','','','']
    
    answers = []

    for fst in range(22):
        string[0] = alphabets[fst]

        for sec in range(23):
            string[1] = alphabets[sec]

            for thd in range(23):
                string[2] = alphabets[thd]

                for foth in range(23):
                    string[3] = alphabets[foth]

                    for fith in range(23):
                        string[4] = alphabets[fith]
                        hsh = hashing(''.join(string))
                        cnt = count_number_of_ONE(str(hsh))
                        if cnt == 7:
                            answers.append(''.join(string))
    print(answers)