premise_marks = [26, 60, 72, 85, 80]
hypothesis_marks = [56, 60, 72, 85, 80]

# the hypothesis refers to the same subjects and marks as the premise
if hypothesis_marks == premise_marks:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif hypothesis_marks!= premise_marks:
    # check if the hypothesis values contradict the premise values
    label = "neutral"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
