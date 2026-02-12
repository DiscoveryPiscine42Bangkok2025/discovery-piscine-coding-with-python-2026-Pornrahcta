from checkmate import checkmate
def main():
    # ตัวอักษรทุกตัวยกเว้น P,B,R,Q,K หมายถึงที่ว่างในกระดาน
    board = """\
    ...R
    .R..
    ..B.
    K.QP\
    """
    checkmate(board)

if __name__ == "__main__":
    main()