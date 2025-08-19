def input_list() -> [str]:
    inputs: [str] = None
    string: str = ""

    inputs = []
    string = input()
    while string != "\n":
        inputs = inputs + [string]
        string = input()
    return inputs

def remove_duplicates(strings: [str]) -> [str]:
    removed: [str] = None
    string: str = ""
    i: int = 0

    def not_in(ys: [str], x: str) -> bool:
        j: int = 0
        y: str = ""
        while j < len(ys):
            y = ys[j]
            if y == x:
                return False
            j = j + 1
        return True

    removed = []
    while i < len(strings):
        string = strings[i]
        if not_in(removed, string):
            removed = removed + [string]
        i = i + 1
    return removed

def main():
    i: int = 0
    unduped: [str] = None

    unduped = remove_duplicates(input_list())
    while i < len(unduped):
        print(unduped[i])
        i = i + 1

main()
