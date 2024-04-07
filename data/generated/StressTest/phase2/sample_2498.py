# Premise: Another survey of 110 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of less than 110 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: contradiction

people_premise = 110
people_hypothesis = 110

# the hypothesis refers to the number of people surveyed in the town of Angie mentioned in the premise
if people_hypothesis < people_premise:
    # check if the number of people surveyed in the hypothesis contradicts the number of people surveyed in the premise
    label = "contradiction"
else:
    # if the number of people surveyed in the hypothesis does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
