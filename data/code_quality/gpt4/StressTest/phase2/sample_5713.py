units_digits_premise = 2
units_digits_hypothesis = 6

# the hypothesis talks about the product of the possible units digits of Sophie Germain primes, referenced also in the premise
if units_digits_hypothesis < units_digits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'units_digits_premise' 
    label = "contradiction"
elif units_digits_hypothesis == units_digits_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of units digits
    # any number of units digits greater than 'units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
