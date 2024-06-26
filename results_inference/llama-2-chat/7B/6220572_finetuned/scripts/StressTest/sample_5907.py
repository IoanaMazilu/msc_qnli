marks_scored_premise = [76, 65, 82, 67, 75]
marks_scored_hypothesis = [46, 65, 82, 67, 75]

# the hypothesis refers to the marks scored in each subject, as mentioned in the premise
for subject, marks_premise in enumerate(marks_scored_premise):
    if marks_scored_hypothesis[subject] <= marks_premise:
        # check if the estimate of'marks_scored_hypothesis' contradicts the marks scored in the premise
        label = "contradiction"
        break
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
