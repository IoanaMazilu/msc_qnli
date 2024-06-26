# define the scores obtained by Reeya in the premise and hypothesis
scores_premise = [55, 67, 76, 82, 85]
scores_hypothesis = [35, 67, 76, 82, 85]

# calculate the average score in the premise and hypothesis
average_premise = sum(scores_premise) / len(scores_premise)
average_hypothesis = sum(scores_hypothesis) / len(scores_hypothesis)

# compare the average scores in the premise and hypothesis
if average_premise!= average_hypothesis:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average scores in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
