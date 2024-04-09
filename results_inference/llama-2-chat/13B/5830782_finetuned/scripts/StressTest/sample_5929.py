english_marks_premise = 46
english_marks_hypothesis = 86
math_marks_premise = 85
math_marks_hypothesis = 85
physics_marks_premise = 92
physics_marks_hypothesis = 92
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 95
biology_marks_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in various subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise:
    # check if the Math marks in the hypothesis contradicts the Math marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the Physics marks in the hypothesis contradicts the Physics marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the Chemistry marks in the hypothesis contradicts the Chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the Biology marks in the hypothesis contradicts the Biology marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the English marks
    # any number of English marks greater than 'english_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
