def pretty_print(board):
    for row in board:
        row_str = ""
        for column in row:
            row_str += f"{str(column):^4} "
        print(row_str)

    print("\n")
