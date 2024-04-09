earned_premise = 4000
earned_hypothesis = 9000

# the hypothesis refers to the amount of money earned by the person in question and Rick
if earned_hypothesis <= earned_premise:
    # check if the estimate of 'earned_hypothesis' contradicts the amount of money earned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money earned
    # any amount of money greater than 'earned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
