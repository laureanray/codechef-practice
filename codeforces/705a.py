if __name__ == "__main__":
    n = int(input())
    strings = []
    for i in range(n):
        if i % 2 == 0:
        # love
            strings.append('I hate')
        else:
            strings.append('I love')

    print(' that '.join(strings), 'it')