# Scores obtained by Nancy in different subjects according to the premise and hypothesis
scores_amer_lit_premise = 86
scores_amer_lit_hypothesis = 66
scores_history_premise = 75
scores_history_hypothesis = 75
scores_home_ec_premise = 52
scores_home_ec_hypothesis = 52
scores_pe_premise = 68
scores_pe_hypothesis = 68
scores_art_premise = 89
scores_art_hypothesis = 89

# the hypothesis refers to the scores Nancy obtained in different subjects, as mentioned in the premise
if scores_amer_lit_hypothesis >= scores_amer_lit_premise:
    # check if the score in American Literature in the hypothesis contradicts the premise
    label = "contradiction"
elif scores_history_hypothesis!= scores_history_premise or scores_home_ec_hypothesis!= scores_home_ec_premise or scores_pe_hypothesis!= scores_pe_premise or scores_art_hypothesis!= scores_art_premise:
    # check if the scores in other subjects in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
