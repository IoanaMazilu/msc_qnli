marks_scored_premise = [46, 65, 82, 67, 75]
marks_scored_hypothesis = [76, 65, 82, 67, 75]

# the hypothesis refers to the marks scored by Shekar in different subjects mentioned in the premise
for marks_score_premise, marks_score_hypothesis in zip(marks_scored_premise, marks_scored_hypothesis):
    if marks_score_hypothesis <= marks_score_premise:
        # check if the hypothesis value contradicts the estimate of more than'marks_score_premise'
        label = "contradiction"
        break
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
