marks_premise = [86, 89, 82, 87, 81]
marks_hypothesis = [86, 89, 82, 87, 81]

# the hypothesis refers to the marks obtained by Dacid in the subjects mentioned in the premise
if any(marks_hypothesis <= marks_premise):
    # check if any of the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # all the marks in the hypothesis are consistent with the marks in the premise, so we can infer entailment
    label = "entailment"

print(label)
