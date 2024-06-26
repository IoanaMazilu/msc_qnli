math_mark_premise = 76
science_mark_premise = 65
social_studies_mark_premise = 82
english_mark_premise = 67
biology_mark_premise = 95

math_mark_hypothesis = 76
science_mark_hypothesis = 65
social_studies_mark_hypothesis = 82
english_mark_hypothesis = 67
biology_mark_hypothesis = 95

# the hypothesis talks about the marks of Shekar in different subjects, also mentioned in the premise
if math_mark_hypothesis <= math_mark_premise or science_mark_hypothesis <= science_mark_premise or social_studies_mark_hypothesis <= social_studies_mark_premise or english_mark_hypothesis <= english_mark_premise or biology_mark_hypothesis <= biology_mark_premise:
    # check if the hypothesis value contradicts the premise marks for any subject
    label = "contradiction"
else:
    # the premise gives exact marks for each subject
    # any marks greater than the premise marks is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
