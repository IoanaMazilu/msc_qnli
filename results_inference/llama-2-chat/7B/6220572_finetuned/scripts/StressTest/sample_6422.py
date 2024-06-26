marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [46, 65, 82, 67, 85]

# the hypothesis refers to the marks obtained by Arun in various subjects, also mentioned in the premise
for i, mark in enumerate(marks_hypothesis):
    # check if the mark value in the hypothesis contradicts the mark value in the premise
    if mark!= marks_premise[i]:
        label = "contradiction"
        break
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
