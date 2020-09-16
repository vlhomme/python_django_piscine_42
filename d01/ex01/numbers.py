if __name__ == '__main__':
    with open("numbers.txt", 'r') as f:
        nbList = f.readline().strip().split(',')
        for element in nbList:
            print(element)
