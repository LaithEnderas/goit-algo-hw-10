# набір монет за замовчуванням
DEFAULT_COINS = [50, 25, 10, 5, 2, 1]

# жадібний алгоритм
def find_coins_greedy(amount, coins=None):
    # повертає словник номінал: кількість, вибираючи найбільші монети спочатку
    if coins is None:
        coins = DEFAULT_COINS
    result = {}
    for c in sorted(coins, reverse=True):
        if amount <= 0:
            break
        k = amount // c
        if k:
            result[c] = k
            amount -= k * c
    return result

# динамічне програмування мінімальна кількість монет
def find_min_coins(amount, coins=None):
    # повертає словник номінал: кількість з мінімальною кількістю монет
    if coins is None:
        coins = sorted(DEFAULT_COINS)
    # dp[i] - мінімальна кількість монет для суми i
    # prev[i] - остання монета яку взяли для суми i
    dp = [float("inf")] * (amount + 1)
    prev = [-1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                prev[i] = c
    # відновлюємо розклад по монетах
    res = {}
    if dp[amount] == float("inf"):
        return res
    x = amount
    while x > 0:
        c = prev[x]
        res[c] = res.get(c, 0) + 1
        x -= c
    return dict(sorted(res.items(), reverse=True))

# невелика перевірка
if __name__ == "__main__":
    amount = 113
    print("сума", amount)
    print("жадібний", find_coins_greedy(amount))
    print("динамічний", find_min_coins(amount))

    # приклад великої суми
    big = 9999
    print("велика сума", big)
    print("жадібний тільки підсумок монет", sum(find_coins_greedy(big).values()))
    print("динамічний тільки підсумок монет", sum(find_min_coins(big).values()))
