n = int(input())
arr = map(int, input().split())
# l = list(set(arr))
# l.remove(max(l))
# print(max(l))

new_arr = sorted(set(arr))
print(new_arr[-2])