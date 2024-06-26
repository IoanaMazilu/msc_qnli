premise_marks = [46, 85, 92, 87, 95]
hypothesis_marks = [86, 85, 92, 87, 95]

# the hypothesis refers to the exact marks obtained by Dacid in each subject
if hypothesis_marks == premise_marks:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif hypothesis_marks!= premise_marks:
    # check if the hypothesis values contradict the premise ones
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
