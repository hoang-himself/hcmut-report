class iostream:
    def __lshift__(self, other):
        print(other, end='')
        return self

    def __repr__(self):
        return ''


if __name__ == "__main__":
    cout = iostream()
    endl = '\n'
    cout << "Hello" << ", " << "World!" << endl
