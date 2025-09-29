import time


def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    if n in (0, 1):
        return 1
    return n * factorial_rec(n - 1)


def run_with_time(func, n: int):
    """ 함수 func을 n에 대해 1회 실행하고 실행 시간 반환 """
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    elapsed = end - start
    return result, elapsed


TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]


def menu():
    while True:
        print("\n====== 팩토리얼 계산기 ======")
        print("1. 반복문으로 계산")
        print("2. 재귀로 계산")
        print("3. 두 방식 모두 실행")
        print("4. 테스트 데이터 실행")
        print("q. 종료")
        choice = input("메뉴 선택 >> ")

        if choice == "q":
            print("프로그램을 종료합니다.")
            break

        elif choice in ("1", "2", "3"):
            n_str = input("n 값(정수, 0 이상)을 입력하세요 >> ")
            try:
                n = int(n_str)
                if n < 0:
                    raise ValueError

                if choice == "1":
                    result, t = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {result}")
                    print(f"[반복] 시간: {t:.6f} s")

                elif choice == "2":
                    result, t = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {result}")
                    print(f"[재귀] 시간: {t:.6f} s")

                elif choice == "3":
                    res_iter, t_iter = run_with_time(factorial_iter, n)
                    res_rec, t_rec = run_with_time(factorial_rec, n)
                    print(f"[반복] {n}! = {res_iter}")
                    print(f"[재귀] {n}! = {res_rec}")
                    print("결과 일치 여부:", res_iter == res_rec)
                    print(f"[반복] 시간: {t_iter:.6f} s | [재귀] 시간: {t_rec:.6f} s")

            except ValueError:
                print(" 올바른 정수를 입력하세요.")
            except RecursionError:
                print(" RecursionError: 재귀 깊이 초과!")

        elif choice == "4":
            print("\n 테스트 데이터 실행 결과")
            for n in TEST_DATA:
                try:
                    res_iter, t_iter = run_with_time(factorial_iter, n)
                    res_rec, t_rec = run_with_time(factorial_rec, n)
                    print(f"\n▶ n={n}")
                    print(f"  [반복] 결과={res_iter}, 시간={t_iter:.6f}초")
                    print(f"  [재귀] 결과={res_rec}, 시간={t_rec:.6f}초")
                    print(f"  일치 여부: {res_iter == res_rec}")
                except RecursionError:
                    print(f"\n▶ n={n}")
                    print("  [재귀] RecursionError 발생 (깊이 초과)")

        else:
            print(" 잘못된 입력입니다. 다시 선택하세요.")


if __name__ == "__main__":
    menu()


