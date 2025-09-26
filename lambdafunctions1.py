log_file = 'logs.txt'
with open(log_file) as f: 
    wystapienia = sum(line.count('ERROR') for line in f)
    # wystapieniai = sum(line.count('DEBUG') for line in f)
    print(f'ERROR:{wystapienia}') # -> u mnie to działa
    # print(f'INFO:{wystapieniai}') # -> u mnie to działa