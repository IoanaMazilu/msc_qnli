math_marks_premise = 16
math_marks_hypothesis = 76
science_marks_premise = 65
science_marks_hypothesis = 65
social_marks_premise = 82
social_marks_hypothesis = 82
english_marks_premise = 62
english_marks_hypothesis = 62
biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis refers to the scores in different subjects mentioned in the premise
if math_marks_hypothesis <= math_marks_premise:
    # check if the score in Mathematics in the hypothesis contradicts the estimate of more than 'math_marks_premise'
    label = "contradiction"
elif science_marks_hypothesis != science_marks_premise or social_marks_hypothesis != social_marks_premise or english_marks_hypothesis != english_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the scores in other subjects in the hypothesis contradict the exact scores mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the score in Mathematics
    # a score in Mathematics greater than 'math_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
