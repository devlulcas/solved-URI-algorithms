#URI 1168 - LEDS
leds = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6
}

n = int(input())
results = []
for i in range(n):
    num = input()
    n_sum = 0
    for letter in num:
        n_sum += leds[letter]
    results.append(f"{n_sum} leds")
for j in range(n):
    print(results[j])
        