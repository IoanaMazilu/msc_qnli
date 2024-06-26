score_marks_premise = [46, 65, 82, 67, 75]
score_marks_hypothesis = [76, 65, 82, 67, 75]

# the hypothesis refers to the marks scored by Shekar in each subject mentioned in the premise
for i in range(len(score_marks_premise)):
    if score_marks_hypothesis[i] < score_marks_premise[i]:
        # check if the score in the 'i-th' subject of the hypothesis contradicts the score in the same subject of the premise
        label = "contradiction"
    elif score_marks_hypothesis[i] > score_marks_premise[i]:
        # check if the score in the 'i-th' subject of the hypothesis is greater than the score in the same subject of the premise
        label = "entailment"
    else:
        # if the scores in the 'i-th' subject of the hypothesis and premise are the same, it is neutral
        label = "neutral"
    break
else:
    label = "neutral"

print(label)
