# 1p 2p 5p 10p 20p 50p 100p(1euro) 200p (2euro)
#Ka� farkl� �ekilde 2 pound olu�abilir?
#200p  pound ka� tane 1 den olu�abilir, ka� tane 2 den olu�abilir, ka� tane 5 ten olu�abilir, ka� tane 10 dan .....

def find_combinations(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

# Hedef say� ve kullan�lacak say�lar
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]


result = find_combinations(target, coins)
print(f"{target} sayisini {coins} sayilarindan olusturmanin {result} farkli yolu vardir.")        