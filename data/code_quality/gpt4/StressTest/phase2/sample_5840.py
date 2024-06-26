average_grade_premise = 75
average_grade_hypothesis = 75

# the hypothesis refers to the average grade after Ella took the test, which is also mentioned in the premise
if average_grade_hypothesis >= average_grade_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
