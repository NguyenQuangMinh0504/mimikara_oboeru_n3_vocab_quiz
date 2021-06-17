import pandas as pd


def add_data():
    data = []
    checking = False
    while not checking:
        kanji = []
        kanji_input = input("Nhap vao kanji")
        kanji.append(kanji_input)
        print(kanji)
        meaning_input = input("Nhap vao meaning")
        meaning = meaning_input.strip().split(',')
        print(meaning)

        spelling_input = input("Nhap vao spelling")
        spelling = spelling_input.strip().split(',')
        print(spelling)

        han_tu = []
        han_tu_input = input("Nhap vao han tu")
        han_tu.append(han_tu_input)
        print(han_tu_input)
        yes_no = input("Y/N")
        if yes_no == "Y":
            checking = False
        else:
            checking = True
        data.append([kanji, meaning, spelling, han_tu])

    df = pd.DataFrame(data)
    writer = pd.ExcelWriter("DATA123.xlsx")
    df.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()
