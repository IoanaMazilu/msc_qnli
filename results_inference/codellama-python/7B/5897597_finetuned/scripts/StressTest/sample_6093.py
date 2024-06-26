units_digits_premise = 9
units_digits_hypothesis = 8

# the hypothesis refers to the units digits of Sophie Germain primes, mentioned also in the premise
if units_digits_hypothesis >= units_digits_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)