from statistics import mean, median, mode

data = list(map(float, input("Enter numbers separated by space: ").split()))

print("Mean:", mean(data))
print("Median:", median(data))
try:
    print("Mode:", mode(data))
except:
    print("Mode: No unique mode found")
