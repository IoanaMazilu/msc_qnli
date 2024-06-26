scores_premise = [50, 60, 70, 80, 80]
scores_hypothesis = [40, 60, 70, 80, 80]
average_premise = sum(scores_premise) / len(scores_premise)
average_hypothesis = sum(scores_hypothesis) / len(scores_hypothesis)

# the hypothesis refers to the scores obtained by Reeya in different subjects, which are also mentioned in the premise
if average_hypothesis!= average_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
