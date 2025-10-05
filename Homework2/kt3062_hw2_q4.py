def e_approx(n):
    sum_approx = 1
    prev_factorial = 1
    for i in range(1,n+1):
        prev_factorial*=i
        sum_approx += ((1)/(prev_factorial))
    return sum_approx

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", curr_approx)
