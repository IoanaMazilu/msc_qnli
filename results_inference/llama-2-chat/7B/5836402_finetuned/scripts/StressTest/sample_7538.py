scores_premise = [40, 60, 70, 80, 80]
scores_hypothesis = [40, 60, 70, 80, 80]
average_premise = sum(scores_premise) / len(scores_premise)
average_hypothesis = 0

# the hypothesis refers to the scores obtained by Reeya in different subjects mentioned in the premise
if average_hypothesis!= average_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
elif scores_hypothesis[0] > scores_premise[0] or scores_hypothesis[1] < scores_premise[1] or scores_hypothesis[2] > scores_premise[2] or scores_hypothesis[3] < scores_premise[3] or scores_hypothesis[4] > scores_premise[4] or scores_hypothesis[5] < scores_premise[5]:
    # check if any of the scores in the hypothesis contradicts the scores in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
