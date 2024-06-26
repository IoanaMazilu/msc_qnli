score_interacional_premise = 4
score_seongnam_premise = 2
score_interacional_hypothesis = 4
score_seongnam_hypothesis = 2

# the hypothesis mentions the score of Internacional and Seongnam, which are also mentioned in the premise
if score_interacional_hypothesis!= score_interacional_premise:
    # check if the score of Internacional in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif score_seongnam_hypothesis!= score_seongnam_premise:
    # check if the score of Seongnam from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
