import sys

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = float(sys.argv[1])
    i = float(sys.argv[2])
    t = float(sys.argv[3])

    print("Simple Interest:", simple_interest(p, i, t))