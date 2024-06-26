 score_premise = 18
score_hypothesis = 38

# the hypothesis talks about the average score of Scott's first four rounds, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis does not contradict the average score in the premise, we can infer entailment
    label = "entailment"

print(label)
