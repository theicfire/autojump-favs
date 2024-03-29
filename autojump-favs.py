import os
import argparse

AUTOJUMP_DIR = '/Users/chase/Library/autojump/autojump.txt'

def clean(filename):
    out = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            num, path = map(lambda x: x.strip(), filter(lambda x: len(x) > 0, line.split('\t')))
            if os.path.exists(path):
                out.append(line)
    with open(filename, 'w') as f:
        f.write(''.join(out))

def list_stars(filename):
    ret = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            num, path = map(lambda x: x.strip(), filter(lambda x: len(x) > 0, line.split('\t')))
            if float(num) >= 20000:
                ret.append(path)
    print(ret)

def set_dir_score(filename, d, score):
    out = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            num, path = map(lambda x: x.strip(), filter(lambda x: len(x) > 0, line.split('\t')))

            if path == d:
                replace = str(score) + '\t' + path + '\n'
                out.append(replace)
            else:
                out.append(line)

    with open(filename, 'w') as f:
        f.write(''.join(out))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('action', type=str, help='star, unstar, clean')
    args = parser.parse_args()

    cwd = os.getcwd()
    if args.action == 'star':
        print('Autojump Starring', cwd)
        set_dir_score(AUTOJUMP_DIR, cwd, 20000)
    elif args.action == 'unstar':
        print('Autojump Unstarring', cwd)
        set_dir_score(AUTOJUMP_DIR, cwd, 0)
    elif args.action == 'list':
        list_stars(AUTOJUMP_DIR)
    else:
        print('Autojump Cleaning')
        clean(AUTOJUMP_DIR)
