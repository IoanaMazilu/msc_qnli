maths_score_premise = 76
maths_score_hypothesis = 46
science_score_premise = 65
science_score_hypothesis = 65
social_studies_score_premise = 82
social_studies_score_hypothesis = 82
english_score_premise = 67
english_score_hypothesis = 67
biology_score_premise = 75
biology_score_hypothesis = 75

# the hypothesis talks about the scores of Shekar in different subjects, referenced also in the premise
if maths_score_hypothesis >= maths_score_premise:
    # check if the hypothesis value contradicts the score in Mathematics
    label = "contradiction"
elif science_score_hypothesis!= science_score_premise:
    # check if the score in Science in the hypothesis contradicts the score in Science reported in the premise
    label = "contradiction"
elif social_studies_score_hypothesis!= social_studies_score_premise:
    # check if the score in Social studies in the hypothesis contradicts the score in Social studies reported in the premise
    label = "contradiction"
elif english_score_hypothesis!= english_score_premise:
    # check if the score in English in the hypothesis contradicts the score in English reported in the premise
    label = "contradiction"
elif biology_score_hypothesis!= biology_score_premise:
    # check if the score in Biology in the hypothesis contradicts the score in Biology reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
