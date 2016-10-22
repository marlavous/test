def plaintext(s):
    res = ''
    i = 0
    while i < len(s):               
        i += int(s[i])   # Skip the number of chars specified

        i += 1
        res += s[i]  # Take the letter after them

        i += 1   # Move on to the next position

    return res

def main():

    print plaintext("0h2ake1zy")
    print plaintext("2xwz")
    print plaintext("0h2zyi2467")

if __name__ == '__main__':
    main()