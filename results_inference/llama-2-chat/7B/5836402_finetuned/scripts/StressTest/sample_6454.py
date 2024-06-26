# defining variables for each subject area's scores in the premise
english_score_premise = 76
mathematics_score_premise = 60
chemistry_score_premise = 72
biology_score_premise = 77
french_score_premise = 55
physics_score_premise = 85

# defining variables for each subject area's scores in the hypothesis
english_score_hypothesis = 66
mathematics_score_hypothesis = 60
chemistry_score_hypothesis = 72
biology_score_hypothesis = 77
french_score_hypothesis = 55
physics_score_hypothesis = 85

# comparing the scores in each subject area
if english_score_premise!= english_score_hypothesis:
    # check if the English score in the hypothesis contradicts the English score in the premise
    label = "contradiction"
elif mathematics_score_premise!= mathematics_score_hypothesis:
    # check if the Mathematics score in the hypothesis contradicts the Mathematics score in the premise
    label = "contradiction"
elif chemistry_score_premise!= chemistry_score_hypothesis:
    # check if the Chemistry score in the hypothesis contradicts the Chemistry score in the premise
    label = "contradiction"
elif biology_score_premise!= biology_score_hypothesis:
    # check if the Biology score in the hypothesis contradicts the Biology score in the premise
    label = "contradiction"
elif french_score_premise!= french_score_hypothesis:
    # check if the French score in the hypothesis contradicts the French score in the premise
    label = "contradiction"
elif physics_score_premise!= physics_score_hypothesis:
    # check if the Physics score in the hypothesis contradicts the Physics score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
