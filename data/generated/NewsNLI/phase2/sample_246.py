# Premise: At least four people were hurt, authorities said, but there were no reports of fatalities.
# Hypothesis: At least four people were reported injured.
# Golden Label: entailment

people_hurt_premise = 4
people_injured_hypothesis = 4

# the hypothesis mentions the number of people injured, which is also referenced in the premise
if people_injured_hypothesis < people_hurt_premise:
    # check if the number of people injured in the hypothesis contradicts the number of people hurt in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

