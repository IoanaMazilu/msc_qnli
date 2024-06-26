premise_marks = [86, 85, 82, 87, 85]
hypothesis_marks = [less than 86, 85, 82, 87, 85]

# check if the hypothesis marks are less than the premise marks
if hypothesis_marks[0] < premise_marks[0]:
    # check if the hypothesis marks for the other subjects are less than the premise marks
    if all(hypothesis_marks[i] < premise_marks[i] for i in range(1, len(hypothesis_marks))):
        # if the hypothesis marks for all subjects are less than the premise marks, we can infer entailment
        label = "entailment"
    else:
        # if the hypothesis marks for some subjects are less than the premise marks, but not all, we can infer contradiction
        label = "contradiction"
else:
    # if the hypothesis marks for the first subject are not less than the premise marks, we can infer neutral
    label = "neutral"

print(label)
