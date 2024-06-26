# define variables for the scores in each subject
english_score_premise = 66
mathematics_score_premise = 60
chemistry_score_premise = 72
biology_score_premise = 77
french_score_premise = 55
physics_score_premise = 85

english_score_hypothesis = 66
mathematics_score_hypothesis = 60
chemistry_score_hypothesis = 72
biology_score_hypothesis = 77
french_score_hypothesis = 55
physics_score_hypothesis = 85

# the hypothesis refers to the scores in each subject mentioned in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the hypothesis value contradicts the English score in the premise
    label = "contradiction"
elif mathematics_score_hypothesis!= mathematics_score_premise:
    # check if the Mathematics score in the hypothesis contradicts the Mathematics score reported in the premise
    label = "contradiction"
elif chemistry_score_hypothesis!= chemistry_score_premise:
    # check if the Chemistry score in the hypothesis contradicts the Chemistry score reported in the premise
    label = "contradiction"
elif biology_score_hypothesis!= biology_score_premise:
    # check if the Biology score in the hypothesis contradicts the Biology score reported in the premise
    label = "contradiction"
elif french_score_hypothesis!= french_score_premise:
    # check if the French score in the hypothesis contradicts the French score reported in the premise
    label = "contradiction"
elif physics_score_hypothesis!= physics_score_premise:
    # check if the Physics score in the hypothesis contradicts the Physics score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
