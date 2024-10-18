# write your code here
lis = []
def header():
    global lis
    level = int(input('Level: '))
    while True:
        if level < 1 or level > 6:
            print('The level should be within the range of 1 to 6')
            level = int(input('Level: '))
        else:
            break
        
    text = input('Text: ')
    st = '#'*level+ ' ' + text + '\n'
    lis.append(st)
    print(''.join(lis))
def link():
    global lis
    label = input('Label: ')
    url = input('Url:')
    st = f'[{label}]({url})'
    lis.append(st)
    print(''.join(lis))
def bold():
    global lis
    text = input('Text: ')
    st = f'**{text}**'
    lis.append(st)
    print(''.join(lis))
def italic():
    global lis
    text = input('Text: ')
    st = f'*{text}*'
    lis.append(st)
    print(''.join(lis))
def plain():
    global lis
    text = input('Text: ')
    lis.append(text)
    print(''.join(lis))
def in_line():
    global lis
    text = input('Text: ')
    st = f"`{text}`"
    lis.append(st)
    print(''.join(lis))
def new_line():
    global lis
    lis.append('\n')
    print(''.join(lis))
    
def description(choice):
    global lis
    num = int(input('Number of rows: '))
    while True:
        if num < 1:
            print('The number of rows should be greater than zero')
            num = int(input('Number of rows: '))
        else:
            break
    if len(lis) != 0:
        lis.append('\n')
    for i in range(1,(num+1)):
        row = input(f'Row #{i}: ')
        if choice == 'ordered-list':
            st = f'{i}. {row}\n'
        else:
            st = f'* {row}\n'
        lis.append(st)
    print(''.join(lis))         

def handler(choice):
    if choice == 'header':
        header()
    elif choice == 'link':
        link()
    elif choice == 'bold':
        bold()
    elif choice == 'italic':
        italic()
    elif choice == 'plain':
        plain()
    elif choice == 'inline-code':
        in_line()
    elif choice == 'new-line':
        new_line()
    elif choice == 'ordered-list' or choice == 'unordered-list':
        description(choice)
    else:
        print('Unknown formatting type or command')
def save_to_file():
    with open('output.md', 'w') as file:
        for i in lis:
            file.write(i)

def markdown():
    stop = True
    fonts = ['plain', 'bold', 'italic','header', 'link', 'inline-code', 'new-line','unordered-list','ordered-list']
    while stop:
        user = input('Choose a formatter: ')
        if user == '!done':
            save_to_file()
            stop = False
        elif user == '!help':
            print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
            print('Special commands: !help !done')
            continue
        elif user in fonts:
            handler(user)
            continue
        else:
            print('Unknown formatting type or command')

markdown()
