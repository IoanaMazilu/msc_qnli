average_score_premise = (66 + 60 + 72 + 77 + 55 + 85) / 6
average_score_hypothesis = (66 + 60 + 72 + 77 + 55 + 85) / 6

# the hypothesis refers to the scores Andrea got in the examination
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis does not contradict the average score in the premise, we can infer entailment
    label = "entailment"

print(label)
