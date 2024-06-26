# define variables for the scores in each subject
english_score_premise = 76
english_score_hypothesis = 66
mathematics_score_premise = 60
mathematics_score_hypothesis = 60
chemistry_score_premise = 72
chemistry_score_hypothesis = 72
biology_score_premise = 77
biology_score_hypothesis = 77
french_score_premise = 55
french_score_hypothesis = 55
physics_score_premise = 85
physics_score_hypothesis = 85

# check if the hypothesis scores contradict the premise ones
if english_score_hypothesis >= english_score_premise:
    label = "contradiction"
elif mathematics_score_hypothesis!= mathematics_score_premise:
    label = "contradiction"
elif chemistry_score_hypothesis!= chemistry_score_premise:
    label = "contradiction"
elif biology_score_hypothesis!= biology_score_premise:
    label = "contradiction"
elif french_score_hypothesis!= french_score_premise:
    label = "contradiction"
elif physics_score_hypothesis!= physics_score_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
