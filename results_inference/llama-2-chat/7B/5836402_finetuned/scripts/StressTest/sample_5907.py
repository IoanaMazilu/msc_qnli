marks_scored_premise = [76, 65, 82, 67, 75]
marks_scored_hypothesis = [46, 65, 82, 67, 75]

# the hypothesis refers to the marks scored by Shekar in various subjects, as mentioned in the premise
for i in range(6):
    if marks_scored_premise[i] <= marks_scored_hypothesis[i]:
        # check if the estimate of'marks_scored_hypothesis[i)' contradicts the mark scored in the premise
        label = "contradiction"
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"

print(label)
