def solution(price, money, count):
    price_sum = count * (count+1) // 2 * price
    
    return 0 if price_sum <= money else price_sum - money