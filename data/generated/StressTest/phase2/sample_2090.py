# Premise: Nancy is standing in the middle of the row at the 6 th position. Can you find out the total number of girls in that row?
# Hypothesis: Nancy is standing in the middle of the row at the 2 th position. Can you find out the total number of girls in that row?
# Golden Label: contradiction

nancy_position_premise = 6
nancy_position_hypothesis = 2

# the hypothesis refers to Nancy's position in the row, which is also mentioned in the premise
if nancy_position_hypothesis != nancy_position_premise:
    # check if the position of Nancy in the hypothesis contradicts the position reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

