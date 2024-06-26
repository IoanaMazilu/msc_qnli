units_digits_premise = 8
units_digits_hypothesis = 4

# the hypothesis refers to the units digits of Sophie Germain primes mentioned in the premise
if units_digits_hypothesis > units_digits_premise:
    # check if the 'units_digits_hypothesis' contradicts the 'units_digits_premise'
    label = "contradiction"
elif units_digits_hypothesis < units_digits_premise:
    # check if the 'units_digits_hypothesis' is less than 'units_digits_premise'
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
