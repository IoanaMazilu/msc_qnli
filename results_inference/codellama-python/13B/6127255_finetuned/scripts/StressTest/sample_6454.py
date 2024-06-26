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

# the hypothesis refers to the scores Andrea got in each subject in an examination, which is also mentioned in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the English score in the hypothesis contradicts the estimate of less than 'english_score_premise'
    label = "contradiction"
elif math_score_hypothesis!= math_score_premise or chemistry_score_hypothesis!= chemistry_score_premise or biology_score_hypothesis!= biology_score_premise or french_score_hypothesis!= french_score_premise or physics_score_hypothesis!= physics_score_premise:
    # check if the scores in other subjects in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the English score
    # any English score less than 'english_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
