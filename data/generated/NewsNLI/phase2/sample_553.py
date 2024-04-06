# Premise: Australia's Matt Jones finished tied with American George McNeill on 12-under in sixth, with five players, including world number three Luke Donald, finishing one shot further back.
# Hypothesis: World number three Luke Donald finishes three shots back on 12-under par.
# Golden Label: neutral

matt_jones_score_premise = -12
george_mcneill_score_premise = -12
luke_donald_score_premise = -11
luke_donald_score_hypothesis = -12

# the hypothesis mentions the score of Luke Donald, which is also mentioned in the premise
# we want to check if the score mentioned in the hypothesis contradicts the score from the premise
if luke_donald_score_hypothesis != luke_donald_score_premise:
    label = "contradiction"
else:
    # if the score of Luke Donald from the hypothesis does not contradict the score from the premise, we can infer entailment
    label = "entailment"

print(label)

