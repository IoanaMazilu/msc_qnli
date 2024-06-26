premise_marks = [86, 89, 82, 87, 81]
hypothesis_marks = [56, 89, 82, 87, 81]

# the hypothesis refers to the marks obtained in the same subjects as the premise
if hypothesis_marks == premise_marks:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif hypothesis_marks!= premise_marks:
    # check if the hypothesis values are consistent with the premise ones
    label = "neutral"
else:
    # the hypothesis values are consistent with the premise ones
    label = "entailment"

print(label)
