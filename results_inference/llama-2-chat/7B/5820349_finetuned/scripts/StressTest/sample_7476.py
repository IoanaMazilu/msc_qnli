units_digits_premise = 8
units_digits_hypothesis = 7

# the hypothesis refers to the possible units digits of Sophie Germain primes mentioned in the premise
if units_digits_premise <= units_digits_hypothesis:
    # check if the estimate of 'units_digits_hypothesis' contradicts the number of possible units digits in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
