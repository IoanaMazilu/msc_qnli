digits_premise = 7
digits_hypothesis = 3

# the hypothesis talks about a different number (3) than the premise (7)
if digits_hypothesis <= digits_premise:
    # check if the hypothesis value contradicts the estimate of 'digits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of digits
    # any number of digits greater than 'digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
