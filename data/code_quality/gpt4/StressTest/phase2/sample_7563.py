wage_premise = 8.00
wage_hypothesis = 8.00
tip_rate_premise = 30
tip_rate_hypothesis = 70

# the hypothesis refers to the wage per hour and tip rate that Jill earns, mentioned in the premise
if wage_premise != wage_hypothesis:
    # check if the wage per hour in the hypothesis contradicts the wage per hour reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis <= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact wage per hour and tip rate
    # any tip rate less than 'tip_rate_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
