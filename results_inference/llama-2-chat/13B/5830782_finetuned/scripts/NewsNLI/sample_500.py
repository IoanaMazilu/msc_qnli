sevilla_score_premise = 3
zaragoza_score_premise = 1
sevilla_score_hypothesis = 3
zaragoza_score_hypothesis = 1

# the hypothesis mentions the score of the game, which is also mentioned in the premise
if sevilla_score_hypothesis!= sevilla_score_premise:
    # check if the score of Sevilla in the hypothesis contradicts the score of Sevilla reported in the premise
    label = "contradiction"
elif zaragoza_score_hypothesis!= zaragoza_score_premise:
    # check if the score of Zaragoza from the hypothesis contradicts the score of Zaragoza in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
