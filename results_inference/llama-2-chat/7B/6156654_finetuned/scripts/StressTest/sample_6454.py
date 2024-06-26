average_score_premise = (76 + 60 + 72 + 77 + 55 + 85) / 6
average_score_hypothesis = (66 + 60 + 72 + 77 + 55 + 85) / 6

# the hypothesis refers to the same scores as the premise, but with different scores for English and Mathematics
if average_score_hypothesis!= average_score_premise:
    # check if the average scores in the hypothesis contradict the average scores in the premise
    label = "contradiction"
else:
    # if the average scores in the hypothesis do not contradict the average scores in the premise, we can infer entailment
    label = "entailment"

print(label)
