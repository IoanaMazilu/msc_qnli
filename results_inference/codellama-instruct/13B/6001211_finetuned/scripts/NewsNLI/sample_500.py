sevilla_score_premise = 3
zaragoza_score_premise = 1
sevilla_score_hypothesis = 3
zaragoza_score_hypothesis = 1

# the hypothesis mentions the score of the Sevilla vs Real Zaragoza game, which is also mentioned in the premise
if sevilla_score_hypothesis!= sevilla_score_premise:
    # check if the score of Sevilla in the hypothesis contradicts the score of Sevilla in the premise
    label = "contradiction"
elif zaragoza_score_hypothesis!= zaragoza_score_premise:
    # check if the score of Real Zaragoza from the hypothesis contradicts the score of Real Zaragoza in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
