average_grade_premise = 76
average_grade_hypothesis = 36

# the hypothesis refers to the average grade after Dan took the test
if average_grade_hypothesis != average_grade_premise:
    # check if the new average grade in the hypothesis contradicts the average grade reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
