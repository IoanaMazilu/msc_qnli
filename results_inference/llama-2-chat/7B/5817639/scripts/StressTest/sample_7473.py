sophie_germain_premise = "A Sophie Germain prime is any positive prime number p for which 2 p + 1 is also prime."
sophie_germain_hypothesis = "A Sophie Germain prime is any positive prime number p for which less than 4 p + 1 is also prime."

# define variables for the premise and hypothesis
p_premise = 0
p_hypothesis = 0

# check if the hypothesis value contradicts the premise value
if sophie_germain_hypothesis < 4 * p_premise + 1:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif sophie_germain_hypothesis > 4 * p_premise + 1:
    # the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise value only provides an estimate for the number of Sophie Germain primes
    # any number of Sophie Germain primes less than 4 times the premise value plus 1 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
