# Premise: Nancy is standing in the middle of the row at the less than 7 th position. Can you find out the total number of girls in that row?
# Hypothesis: Nancy is standing in the middle of the row at the 6 th position. Can you find out the total number of girls in that row?
# Golden Label: neutral

nancy_position_premise = 7
nancy_position_hypothesis = 6

# the hypothesis refers to Nancy's position in the row mentioned in the premise
if nancy_position_hypothesis >= nancy_position_premise:
    # check if the hypothesis position contradicts the estimate of 'less than 7th position'
    label = "contradiction"
elif nancy_position_hypothesis < nancy_position_premise:
    # if the hypothesis position doesn't contradict the premise position, we can infer entailment
    label = "entailment"

print(label)

