# Premise: In Italy, Turin giants Juventus have also made a fine start to the season with their second straight win -- beating Udinese 4-1.
# Hypothesis: Champions Juventus set pace in Serie A with 4-1 win at Udinese.
# Golden Label: neutral

juventus_score_premise = 4
udinese_score_premise = 1
juventus_score_hypothesis = 4
udinese_score_hypothesis = 1

# the hypothesis mentions the scores of Juventus and Udinese, which are also mentioned in the premise
if juventus_score_hypothesis != juventus_score_premise:
    # check if Juventus' score in the hypothesis contradicts Juventus' score reported in the premise
    label = "contradiction"
elif udinese_score_hypothesis != udinese_score_premise:
    # check if Udinese's score from the hypothesis contradicts Udinese's score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

