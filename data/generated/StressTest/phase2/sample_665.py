# Premise: Suraj has a certain average of runs for 14 innings.
# Hypothesis: Suraj has a certain average of runs for 84 innings.
# Golden Label: contradiction

innings_premise = 14
innings_hypothesis = 84

# the hypothesis refers to the number of innings mentioned in the premise
if innings_hypothesis != innings_premise:
    # check if the number of innings in the hypothesis contradicts the number of innings reported in the premise
    label = "contradiction"
else:
    # if the number of innings in the hypothesis does not contradict the number of innings in the premise, we can infer entailment
    label = "entailment"

print(label)

