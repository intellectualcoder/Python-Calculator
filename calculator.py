#x = float(input("what's x? "))
#y = float(input("what's y? "))

#z = round(x + y)
#z = round(x / y, 2)
#z = x / y

#print(f"{z:.2f}")

def main():
    x = int(input("whats x? "))
    print("x squared is", square(x))

def square(n) :
        return n * n

main()