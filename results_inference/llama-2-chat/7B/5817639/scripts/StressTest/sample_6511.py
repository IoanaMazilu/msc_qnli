digits_premise = 5
digits_hypothesis = 7

# the hypothesis talks about a different number of digits than the premise
if digits_hypothesis <= digits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'digits_premise' digits
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of digits
    # any number of digits greater than 'digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
