from checkmate import checkmate
def main():
    # Every character except P,B,R,Q,K means empty in board
    board = """\
    ....
    .R..
    ..B.
    K...\
    """
    checkmate(board)

if __name__ == "__main__":
    main()