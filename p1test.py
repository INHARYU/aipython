def main():
    # 사용자로부터 두 정수 A와 B를 입력받음
    A, B = map(int, input("두 정수를 입력하세요 (공백으로 구분): ").split())
    
    # A와 B의 합을 계산하여 출력
    sum = A + B
    print("두 정수의 합은:", sum)

if __name__ == "__main__":
    main()
