 score_premise = 58
score_hypothesis = 78

# the hypothesis talks about Scott's average golf score, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis does not contradict the average score in the premise, we can infer entailment
    label = "entailment"

print(label)
