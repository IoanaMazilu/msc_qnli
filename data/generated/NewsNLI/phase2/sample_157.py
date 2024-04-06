# Premise: West Ham recovered from being 3-0 down at halftime to rescue a draw away at relegation rivals West Bromwich Albion.
# Hypothesis: West Ham score three second-half goals to rescue a 3-3 draw at West Brom.
# Golden Label: entailment

score_premise = 3
score_hypothesis = 3

# the hypothesis mentions the score of West Ham in the second half, which is also referenced in the premise
if score_hypothesis != score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis score does not contradict the premise score, we can infer entailment
    label = "entailment"

print(label)

