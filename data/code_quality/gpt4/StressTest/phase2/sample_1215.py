prime_premise = 2
prime_hypothesis = 5

# the hypothesis mentions a different multiplier for the prime number p than the premise
if prime_hypothesis > prime_premise:
    # check if the multiplier in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif prime_hypothesis != prime_premise:
    # check if the multiplier in the hypothesis is different than the one in the premise
    label = "neutral"
else:
    # if the multiplier in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
