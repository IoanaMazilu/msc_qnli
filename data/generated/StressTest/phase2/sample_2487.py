# Premise: Thomas worked in the factory @ 4550/- per week. Owner told him to give the amount after one month.
# Hypothesis: Thomas worked in the factory @ less than 7550/- per week. Owner told him to give the amount after one month.
# Golden Label: entailment

wage_premise = 4550
wage_hypothesis = 7550

# the hypothesis talks about Thomas' wage per week, which is also mentioned in the premise
if wage_hypothesis <= wage_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif wage_hypothesis > wage_premise:
    # the premise gives a specific value for the wage
    # a wage less than 'wage_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

