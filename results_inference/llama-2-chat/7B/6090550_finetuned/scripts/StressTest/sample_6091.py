# the premise and hypothesis are about the same concept of Sophie Germain primes

# the hypothesis refers to the same condition as the premise, but with a different number (2p+1)
# we need to check if the condition in the hypothesis contradicts the condition in the premise
if p in [2, 3]:
    # if p is less than or equal to 2, then the hypothesis condition contradicts the premise condition
    label = "contradiction"
else:
    # if p is greater than 3, then the hypothesis condition is entailed by the premise condition
    label = "entailment"

print(label)
