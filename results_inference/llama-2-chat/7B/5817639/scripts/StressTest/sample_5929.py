marks_premise = [46, 85, 92, 87, 95]
marks_hypothesis = [86, 85, 92, 87, 95]

# the hypothesis refers to the marks obtained by Dacid in the subjects mentioned in the premise
if any(marks_hypothesis <= marks_premise):
    # check if any of the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
elif any(marks_hypothesis - marks_premise):
    # check if any of the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
