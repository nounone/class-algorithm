def find_max(A):
    n= len(A)
    move_count = 0
    comp_count = 0

    max_val = A[0]
    move_count += 1

    for i in range(1,n):
        comp_count += 1
        if A[i] > max_val:
            max_val = A[i]
            move_count += 1
    return max_val, comp_count, move_count


if __name__ == "__main__":
    data = [3, 9, 2, 7, 5, 10, 4]
    result, comp, move = find_max(data)
    print(f"비교연산 횟수: {comp}, & 이동연산횟수: {move}")