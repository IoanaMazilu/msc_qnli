average_grade_premise = 77
average_grade_hypothesis = 77

# the hypothesis refers to the new average grade mentioned in the premise
if average_grade_hypothesis >= average_grade_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
