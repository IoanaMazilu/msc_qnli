# Premise: Real Madrid failed to capitalize on their rivals slip up, drawing 1-1 at Zaragoza.
# Hypothesis: Real Madrid also draw at Zaragoza ; Malaga win 3-1 at Rayo Vallecano.
# Golden Label: neutral

real_madrid_score_premise = 1
real_madrid_score_hypothesis = 1
zaragoza_score_premise = 1
zaragoza_score_hypothesis = 1

# the hypothesis mentions the score of the Real Madrid and Zaragoza game, which is also mentioned in the premise
if real_madrid_score_hypothesis != real_madrid_score_premise:
    # check if the Real Madrid's score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif zaragoza_score_hypothesis != zaragoza_score_premise:
    # check if the Zaragoza's score from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

