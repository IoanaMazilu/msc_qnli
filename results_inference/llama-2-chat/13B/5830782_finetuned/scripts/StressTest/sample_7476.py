units_digits_premise = 8
units_digits_hypothesis = 7

# the hypothesis refers to the number of units digits of Sophie Germain primes mentioned in the premise
if units_digits_hypothesis >= units_digits_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
