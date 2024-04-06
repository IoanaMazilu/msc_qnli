# Premise: The superb victory, owing much to two-goal Alain Traore, left them in pole position in Group C after holders Zambia and Nigeria drew 1-1 in the early kick off in Rustenburg.
# Hypothesis: Holders Zambia and Nigeria drew 1-1 in earlier match.
# Golden Label: neutral

zambia_nigeria_score_premise = 1
zambia_nigeria_score_hypothesis = 1

# the hypothesis mentions the match between Zambia and Nigeria, which is also referenced in the premise
# the score in the hypothesis matches the score in the premise
if zambia_nigeria_score_hypothesis != zambia_nigeria_score_premise:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the score in the hypothesis does not contradict the score in the premise, we can infer entailment
    label = "entailment"

print(label)

