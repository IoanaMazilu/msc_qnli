# Premise: Earlier, South American champions Internacional took third place with a 4-2 win over Seongnam Ilhwa Chunma of South Korea with Alecsandro scoring twice.
# Hypothesis: Internacional of Brazil beat Seongnam Ilhwa Chunma 4-2 in third place playoff.
# Golden Label: entailment

intl_score_premise = 4
seongnam_score_premise = 2
intl_score_hypothesis = 4
seongnam_score_hypothesis = 2

# the hypothesis mentions the scores of the third place playoff game, which are also mentioned in the premise
if intl_score_hypothesis != intl_score_premise:
    # check if the score of Internacional in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif seongnam_score_hypothesis != seongnam_score_premise:
    # check if the score of Seongnam Ilhwa Chunma from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)

