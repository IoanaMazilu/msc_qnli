# Score range comparison
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [less_than(8), 2, 3, 4, 5]

# Check if the score ranges in the hypothesis contradict the scores in the premise
if scores_hypothesis[0]!= scores_premise[0]:
    label = "contradiction"
elif scores_hypothesis[1]!= scores_premise[1]:
    label = "contradiction"
elif scores_hypothesis[2]!= scores_premise[2]:
    label = "contradiction"
elif scores_hypothesis[3]!= scores_premise[3]:
    label = "contradiction"
elif scores_hypothesis[4]!= scores_premise[4]:
    label = "contradiction"
elif scores_hypothesis[5]!= scores_premise[5]:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
