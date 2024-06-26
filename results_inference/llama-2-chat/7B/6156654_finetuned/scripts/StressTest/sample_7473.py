p = 2
if p > 4:
    # the hypothesis refers to the value of p
    # any positive prime number less than 4 is not a Sophie Germain prime
    # since 4 is less than 4 p + 1, it is not a Sophie Germain prime
    label = "contradiction"
else:
    # any positive prime number p for which 2 p + 1 is also prime is a Sophie Germain prime
    # since 2 is less than 4, it is a Sophie Germain prime
    label = "entailment"

print(label)
