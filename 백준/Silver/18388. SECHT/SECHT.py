decode = {'Q':'W',
          'W':'E',
          'E':'R',
          'R':'T',
          'T':'Y',
          'Y':'U',
          'U':'I',
          'I':'O',
          'O':'P',
          'A':'S',
          'S':'D',
          'D':'F',
          'F':'G',
          'G':'H',
          'H':'J',
          'J':'K',
          'K':'L',
          'Z':'X',
          'X':'C',
          'C':'V',
          'V':'B',
          'B':'N',
          'N':'M'}

code = input()
answer = ''
for c in code:
    if c in decode:
        answer += decode[c]
    else:
        answer += c
print(answer)
