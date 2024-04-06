# Premise: Juventus'nearest rivals AC Milan kept up the pressure with a 4-1 at Siena.
# Hypothesis: AC Milan also win, defeating Siena 4-1.
# Golden Label: neutral

ac_milan_score_premise = 4
siena_score_premise = 1
ac_milan_score_hypothesis = 4
siena_score_hypothesis = 1

# the hypothesis mentions the game score between AC Milan and Siena, which is also referenced in the premise
if ac_milan_score_hypothesis != ac_milan_score_premise:
    # check if the AC Milan score in the hypothesis contradicts the AC Milan score reported in the premise
    label = "contradiction"
elif siena_score_hypothesis != siena_score_premise:
    # check if the Siena score from the hypothesis contradicts the Siena score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

