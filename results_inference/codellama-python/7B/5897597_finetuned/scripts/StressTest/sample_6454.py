# defining the scores in the premise and hypothesis
english_score_premise = 76
english_score_hypothesis = 66
math_score_premise = 60
math_score_hypothesis = 60
chemistry_score_premise = 72
chemistry_score_hypothesis = 72
biology_score_premise = 77
biology_score_hypothesis = 77
french_score_premise = 55
french_score_hypothesis = 55
physics_score_premise = 85
physics_score_hypothesis = 85

# comparing the scores in the premise and hypothesis
if english_score_premise <= english_score_hypothesis:
    # check if the English score in the hypothesis contradicts the English score in the premise
    label = "contradiction"
elif math_score_premise!= math_score_hypothesis:
    # check if the Math score in the hypothesis contradicts the Math score in the premise
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
    # if the hypothesis scores do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
