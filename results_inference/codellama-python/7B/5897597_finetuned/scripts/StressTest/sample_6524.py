# defining the scores obtained by Reeya in the premise and hypothesis
scores_premise = [55, 67, 76, 82, 85]
scores_hypothesis = [35, 67, 76, 82, 85]

# comparing the scores obtained by Reeya in the premise and hypothesis
if scores_premise!= scores_hypothesis:
    # if the scores obtained by Reeya in the premise and hypothesis are not equal, then it's a contradiction
    label = "contradiction"
else:
    # if the scores obtained by Reeya in the premise and hypothesis are equal, then it's an entailment
    label = "entailment"

print(label)
