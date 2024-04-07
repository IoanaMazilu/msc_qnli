# Premise: If Albert’s monthly earnings rise by 14 %, he would earn $678.
# Hypothesis: If Albert’s monthly earnings rise by less than 74 %, he would earn $678.
# Golden Label: entailment

earnings_increase_premise = 14
earnings_increase_hypothesis = 74
earnings_result = 678

# the hypothesis refers to the same scenario as the premise, but with a different increase in earnings
if earnings_increase_hypothesis <= earnings_increase_premise:
    # check if the increase in earnings specified by the hypothesis contradicts the increase stated in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the increase in earnings
    # any increase greater than 'earnings_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

