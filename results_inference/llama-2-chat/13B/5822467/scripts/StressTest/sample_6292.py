marks_premise = [46, 65, 82, 67, 85]
marks_hypothesis = [76, 65, 82, 67, 85]

# compare the premise and hypothesis marks
for i, mark in enumerate(marks_premise):
    if mark <= marks_hypothesis[i]:
        # check if the estimate of'marks_hypothesis[i]' contradicts the premise mark
        label = "contradiction"
        break
    elif marks_hypothesis[i]!= marks_premise[i]:
        # check if the hypothesis mark contradicts the premise mark
        label = "contradiction"
        break
    else:
        # if the hypothesis marks and estimates do not contradict the premise marks, we can infer entailment
        label = "entailment"
        break

print(label)
