earned_premise = 9000
earned_hypothesis = 9000

# the hypothesis refers to the amount earned at the end of one year
if earned_hypothesis <= earned_premise:
    # check if the hypothesis value contradicts the estimate of 'earned_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount earned
    # any amount less than 'earned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
