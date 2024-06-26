units_digits_premise = 8
units_digits_hypothesis = 4

# the hypothesis refers to the possible units digits of Sophie Germain primes mentioned in the premise
if units_digits_hypothesis > units_digits_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif units_digits_hypothesis < units_digits_premise:
    # check if the hypothesis value is less than the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, we can infer neutrality
    label = "neutral"

print(label)
