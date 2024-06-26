english_marks_premise = 46
math_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in various subjects mentioned in the premise

if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in hypothesis contradict the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise or physics_marks_hypothesis != physics_marks_premise:
    # check if the marks in other subjects in hypothesis contradict the marks mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the English marks and exact marks for other subjects
    # any number of English marks greater than 'english_marks_premise' and equal marks in other subjects is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
