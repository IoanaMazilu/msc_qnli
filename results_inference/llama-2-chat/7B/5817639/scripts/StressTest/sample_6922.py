earned_premise = 810
earned_hypothesis = 210

# the hypothesis refers to the amount of money earned, which is also referred to in the premise
if earned_hypothesis <= earned_premise:
    # check if the hypothesis value contradicts the estimate of 'earned_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money earned
    # any amount of money earned greater than 'earned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
