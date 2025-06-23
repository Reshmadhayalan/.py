def simple_interest(p, t, g, s):
    r = 15 if s.lower() == 'y' else 12 if g.lower() == 'm' else 10
    return (p * r * t) / 100

p = float(input())
t = int(input())
g = input()
s = input()

print("Interest:", int(simple_interest(p, t, g, s)))
