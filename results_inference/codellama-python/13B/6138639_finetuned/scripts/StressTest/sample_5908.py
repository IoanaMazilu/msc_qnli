math_score_premise = 46
math_score_hypothesis = 76
science_score_premise = 65
science_score_hypothesis = 65
social_studies_score_premise = 82
social_studies_score_hypothesis = 82
english_score_premise = 67
english_score_hypothesis = 67
biology_score_premise = 75
biology_score_hypothesis = 75

# the hypothesis talks about the scores of Shekar in different subjects, referenced also in the premise
if math_score_hypothesis <= math_score_premise:
    # check if the hypothesis value contradicts the estimate of more than'math_score_premise'
    label = "contradiction"
elif science_score_hypothesis!= science_score_premise:
    # check if the science score in the hypothesis contradicts the science score reported in the premise
    label = "contradiction"
elif social_studies_score_hypothesis!= social_studies_score_premise:
    # check if the social studies score in the hypothesis contradicts the social studies score reported in the premise
    label = "contradiction"
elif english_score_hypothesis!= english_score_premise:
    # check if the english score in the hypothesis contradicts the english score reported in the premise
    label = "contradiction"
elif biology_score_hypothesis!= biology_score_premise:
    # check if the biology score in the hypothesis contradicts the biology score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any scores greater than'math_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
