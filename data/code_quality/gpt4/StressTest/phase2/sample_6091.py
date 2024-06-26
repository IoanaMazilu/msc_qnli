prime_premise = 3
prime_hypothesis = 2

# both premise and hypothesis are talking about the same concept of "Sophie Germain" prime
if prime_premise != prime_hypothesis:
    # check if the prime number in the hypothesis contradicts the prime number in the premise
    label = "contradiction"
else:
    # if the prime numbers in both hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
