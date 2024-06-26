# define variables for the entities in the premise and hypothesis
sevilla_score_premise = 3
zaragoza_score_premise = 1
sevilla_score_hypothesis = 3
zaragoza_score_hypothesis = 1

# the hypothesis mentions the final score of the match, which is also referenced in the premise
if sevilla_score_hypothesis!= sevilla_score_premise:
    # check if the final score of Sevilla in the hypothesis contradicts the final score reported in the premise
    label = "contradiction"
elif zaragoza_score_hypothesis!= zaragoza_score_premise:
    # check if the final score of Zaragoza in the hypothesis contradicts the final score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
