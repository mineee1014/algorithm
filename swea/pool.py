def func(i,cost):
    global min_price
    if cost >= min_price: return

    if i > 11:
        min_price = cost
        return

    func(i+1, cost + plan[i]*price[0])
    func(i+1, cost + price[1])
    func(i+3, cost + price[2])


T = int(input())
for tc in range(1,T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_price = price[3]
    func(0,0)
    print(f'#{tc} {min_price}')