rich_people_premise = 85
rich_people_hypothesis = 85

# the premise and hypothesis mention the number of richest people and their wealth
if rich_people_hypothesis == rich_people_premise:
    # check if the number of richest people in the hypothesis contradicts the number of richest people in the premise
    label = "entailment"
elif rich_people_hypothesis > rich_people_premise:
    # check if the estimated number of richest people in the hypothesis contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives an estimate for the number of richest people, and any estimate in the hypothesis greater or equal to that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
