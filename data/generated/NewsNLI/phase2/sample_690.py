# Premise: Mexico are odds on to join Uruguay in Brazil after they took a commanding 5-1 lead in their playoff with New Zealand.
# Hypothesis: Mexico thrash New Zealand 5-1 in first leg of their World Cup playoff.
# Golden Label: neutral

mexico_score_premise = 5
newzealand_score_premise = 1
mexico_score_hypothesis = 5
newzealand_score_hypothesis = 1

# the hypothesis mentions the scores of Mexico and New Zealand, which are also mentioned in the premise
if mexico_score_hypothesis != mexico_score_premise:
    # check if the score of Mexico in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif newzealand_score_hypothesis != newzealand_score_premise:
    # check if the score of New Zealand from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)

