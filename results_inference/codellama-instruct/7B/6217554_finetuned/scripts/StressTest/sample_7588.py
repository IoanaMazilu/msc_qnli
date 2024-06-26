# define variables for the scores in each subject
french_score_premise = 46
french_score_hypothesis = 86
geography_score_premise = 75
geography_score_hypothesis = 75
art_score_premise = 72
art_score_hypothesis = 72
design_score_premise = 63
design_score_hypothesis = 63
history_score_premise = 65
history_score_hypothesis = 65
phys_education_score_premise = 65
phys_education_score_hypothesis = 65

# check if the hypothesis scores contradict the premise ones
if french_score_hypothesis <= french_score_premise:
    label = "contradiction"
elif geography_score_hypothesis!= geography_score_premise:
    label = "contradiction"
elif art_score_hypothesis!= art_score_premise:
    label = "contradiction"
elif design_score_hypothesis!= design_score_premise:
    label = "contradiction"
elif history_score_hypothesis!= history_score_premise:
    label = "contradiction"
elif phys_education_score_hypothesis!= phys_education_score_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
