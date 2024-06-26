inter_score_premise = 4
seongnam_score_premise = 2
inter_score_hypothesis = 4
seongnam_score_hypothesis = 2

# the hypothesis mentions the score of the game between Internacional and Seongnam Ilhwa Chunma, which is also mentioned in the premise
if inter_score_hypothesis!= inter_score_premise:
    # check if the score of Internacional in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif seongnam_score_hypothesis!= seongnam_score_premise:
    # check if the score of Seongnam Ilhwa Chunma from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
