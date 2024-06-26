internacional_score_premise = 4
seongnam_score_premise = 2
internacional_score_hypothesis = 4
seongnam_score_hypothesis = 2

# the hypothesis mentions the score of the match between Internacional and Seongnam Ilhwa Chunma, which is also mentioned in the premise
if internacional_score_hypothesis!= internacional_score_premise:
    # check if the score of Internacional in the hypothesis contradicts the score of Internacional reported in the premise
    label = "contradiction"
elif seongnam_score_hypothesis!= seongnam_score_premise:
    # check if the score of Seongnam Ilhwa Chunma from the hypothesis contradicts the score of Seongnam Ilhwa Chunma in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
