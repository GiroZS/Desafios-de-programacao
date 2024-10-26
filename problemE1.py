def achaDivisores(n):
    divisores = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisores.add(i)
            divisores.add(n // i)
    divisores.add(n)
    return divisores

def max_friendly_sum(A):
    all_divisors = set()
    
    # Collect divisors for each number in A
    for number in A:
        all_divisors.update(achaDivisores(number))
    
    # Filter out divisors <= 1
    all_divisors = {d for d in all_divisors if d > 1}
    
    max_sum = 0
    # Check sum of multiples for each divisor
    for k in all_divisors:
        current_sum = sum(x for x in A if x % k == 0)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


N = int(input())
A = []
for _ in range(N):
    A.append(int(input())) 
print(max_friendly_sum(A))
