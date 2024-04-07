# Premise: NHAI employs 100 men to build a highway of 2 km in 50 days working 8 hours a day.
# Hypothesis: NHAI employs 200 men to build a highway of 2 km in 50 days working 8 hours a day.
# Golden Label: contradiction

men_premise = 100
men_hypothesis = 200

# the hypothesis refers to the number of men employed by NHAI, also mentioned in the premise
if men_hypothesis != men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

