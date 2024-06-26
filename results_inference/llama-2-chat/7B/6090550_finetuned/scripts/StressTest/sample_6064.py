english_marks_premise = 16
math_marks_premise = 89
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 81

english_marks_hypothesis = 86
math_marks_hypothesis = 89
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 81

# the hypothesis talks about the marks obtained by Dacid in different subjects
if english_marks_premise!= english_marks_hypothesis:
    # check if the English marks in the hypothesis contradict the English marks in the premise
    label = "contradiction"
elif math_marks_premise!= math_marks_hypothesis:
    # check if the Math marks in the hypothesis contradict the Math marks in the premise
    label = "contradiction"
elif physics_marks_premise!= physics_marks_hypothesis:
    # check if the Physics marks in the hypothesis contradict the Physics marks in the premise
    label = "contradiction"
elif chemistry_marks_premise!= chemistry_marks_hypothesis:
    # check if the Chemistry marks in the hypothesis contradict the Chemistry marks in the premise
    label = "contradiction"
elif biology_marks_premise!= biology_marks_hypothesis:
    # check if the Biology marks in the hypothesis contradict the Biology marks in the premise
    label = "contradiction"
else:
    # if the English, Math, Physics, Chemistry and Biology marks in the hypothesis do not contradict the ones in the premise
    # then the hypothesis can be entailed from the premise
    label = "entailment"

print(label)
