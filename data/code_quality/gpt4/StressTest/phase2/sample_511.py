english_marks_premise = 66
math_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis talks about the marks obtained by Dacid in various subjects
# these marks are also referenced in the premise

if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradict the premise
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the marks in other subjects in the hypothesis contradict the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the English marks
    # any number greater than 'english_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
