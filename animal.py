import sys

def dog():
    print('Baw')

def default():
    print('Hello')

def main():
    if sys.argv[1] == 'dog':
        Dog()
    else:
        default()

if __name__ == '__main__':
    main()
