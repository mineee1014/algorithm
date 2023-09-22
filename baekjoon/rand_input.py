import random

def generate_random_chessboard(size):
    chessboard = []
    for _ in range(size):
        row = [random.randint(0, 1) for _ in range(size)]
        chessboard.append(row)
    return chessboard

def print_chessboard(chessboard):
    for row in chessboard:
        print(" ".join(map(str, row)))

def main():
    size = int(input("체스판 크기를 입력하세요: "))
    random_chessboard = generate_random_chessboard(size)
    print(size)
    print_chessboard(random_chessboard)

if __name__ == "__main__":
    main()
