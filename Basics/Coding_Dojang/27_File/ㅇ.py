fw = open('hello2.txt', 'w')

with open('hello.txt') as f :
    lines = f.readlines()
    for line in lines :
        if line[0].strip(',.\n') != '0' :
                fw.write(line)
        else :
            continue