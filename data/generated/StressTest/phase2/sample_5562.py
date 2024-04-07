# Premise: If Albert’s monthly earnings rise by 27 %, he would earn $567.
# Hypothesis: If Albert’s monthly earnings rise by less than 87 %, he would earn $567.
# Golden Label: entailment

earnings_rise_premise = 27
earnings_rise_hypothesis = 87
earnings_after_rise = 567

# the hypothesis refers to the percentage of the earnings rise and the final amount of earnings, both mentioned in the premise
if earnings_rise_hypothesis < earnings_rise_premise:
    # check if the percentage of earnings rise in the hypothesis contradicts that in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the earnings after a specific percentage rise
    # if the earnings rise by less than 'earnings_rise_hypothesis', the final earnings cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

