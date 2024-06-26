# scores obtained by Renee in the premise
scores_premise = [71, 57, 61, 80, 88]
# scores obtained by Renee in the hypothesis
scores_hypothesis = [51, 57, 61, 80, 88]

# calculate averages for premise and hypothesis
average_premise = sum(scores_premise) / len(scores_premise)
average_hypothesis = sum(scores_hypothesis) / len(scores_hypothesis)

# compare averages
if average_premise != average_hypothesis:
    # if averages are not the same, we have a contradiction
    label = "contradiction"
else:
    # if averages are the same, we have entailment
    label = "entailment"

print(label)
