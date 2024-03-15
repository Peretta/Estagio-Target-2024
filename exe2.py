def fibonacci(n):
    if n <= 0:
        return "O número deve ser maior que 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 8
resp = ""
print("Sequência de Fibonacci até o {}º termo:".format(n))

for i in range(1, n+1):
    resp = resp + str(fibonacci(i)) + " "

print(resp)
if str(n) in resp:
    print("{} está presente na sequencia fibonacci".format(n))