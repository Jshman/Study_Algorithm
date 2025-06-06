e, j, m = input().split()

if e == 'Rock':
    if j == 'Rock':
        if m in ['Rock', 'Scissors']:
            print("Youngwoo")
        else:
            print("Minjung")
    elif j == 'Scissors': #e 한테 졌음
        if m in ['Rock', 'Paper']:
            print("Youngwoo")
        elif m == 'Scissors':
            print("Eunyoung")
    else: #보자기
        if m in ['Scissors', 'Paper']:
            print('Youngwoo')
        else:
            print("Jinha")

elif e == 'Scissors':
    if j == 'Rock':
        if m in ['Rock', 'Paper']:
            print("Youngwoo")
        else:
            print("Jinha")
    elif j == 'Scissors':
        if m in ['Scissors', 'Paper']:
            print("Youngwoo")
        else:
            print("Minjung")
    else: #보자기
        if m in ['Scissors', 'Rock']:
            print("Youngwoo")
        else:
            print("Eunyoung")
else: #보자기
    if j == 'Rock':
        if m in ['Scissors', 'Paper']:
            print("Youngwoo")
        else:
            print('Eunyoung')
    elif j == 'Scissors':
        if m in ['Scissors', 'Rock']:
            print("Youngwoo")
        else:
            print("Jinha")
    else:
        if m in ['Paper', 'Rock']:
            print("Youngwoo")
        else:
            print("Minjung")