marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [60, 50, 70, 60, 75]

# the hypothesis talks about the marks obtained by David in 6 subjects
if any(marks_hypothesis <= marks_premise[i] for i in range(6)):
    # check if any of the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # none of the hypothesis values contradict the premise values, so we can infer entailment
    label = "entailment"

print(label)
