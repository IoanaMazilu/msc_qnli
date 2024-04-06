# Premise: Second-placed Nancy celebrated their 40th anniversary with a 1-0 win over Girondins Bordeaux.
# Hypothesis: Nancy stay second by beating Bordeaux 1-0.
# Golden Label: neutral

nancy_position_premise = 2
nancy_position_hypothesis = 2
nancy_score_premise = 1
nancy_score_hypothesis = 1

# the hypothesis mentions Nancy's position and the score, which are also mentioned in the premise
if nancy_position_hypothesis != nancy_position_premise:
    # check if the position of Nancy in the hypothesis contradicts the position of Nancy in the premise
    label = "contradiction"
elif nancy_score_hypothesis != nancy_score_premise:
    # check if the score from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

