bright_score_premise = 0.4
bivi_score_premise = 0.65
lisa_score_premise = 0.45

bright_score_hypothesis = 0.6
bivi_score_hypothesis = 0.65
lisa_score_hypothesis = 0.45

if bright_score_hypothesis <= bright_score_premise:
    label = "contradiction"
elif bivi_score_hypothesis!= bivi_score_premise:
    label = "contradiction"
elif lisa_score_hypothesis!= lisa_score_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
