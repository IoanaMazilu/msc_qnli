nancy_marks_premise = [66, 75, 52, 68, 89]
nancy_marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis refers to the marks obtained by Nancy in certain subjects, which are also mentioned in the premise
for i in range(6):
    if nancy_marks_premise[i] >= nancy_marks_hypothesis[i]:
        # check if the premise value is greater than or equal to the hypothesis value
        label = "entailment"
    else:
        # if the premise value is less than the hypothesis value, it contradicts the premise
        label = "contradiction"
    break
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
