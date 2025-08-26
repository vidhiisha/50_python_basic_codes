def fibonacci(n):
    seq = [0,1]
    while len(seq)<n:
        seq.append(seq[-1]+seq[-2])
    return seq[:n]

print(fibonacci(30))