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

# the hypothesis talks about the scores of Andrea in different subjects, referenced also in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'english_score_premise'
    label = "contradiction"
elif math_score_hypothesis!= math_score_premise:
    # check if the score in Math in the hypothesis contradicts the score in Math reported in the premise
    label = "contradiction"
elif chemistry_score_hypothesis!= chemistry_score_premise:
    # check if the score in Chemistry in the hypothesis contradicts the score in Chemistry reported in the premise
    label = "contradiction"
elif biology_score_hypothesis!= biology_score_premise:
    # check if the score in Biology in the hypothesis contradicts the score in Biology reported in the premise
    label = "contradiction"
elif french_score_hypothesis!= french_score_premise:
    # check if the score in French in the hypothesis contradicts the score in French reported in the premise
    label = "contradiction"
elif physics_score_hypothesis!= physics_score_premise:
    # check if the score in Physics in the hypothesis contradicts the score in Physics reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
