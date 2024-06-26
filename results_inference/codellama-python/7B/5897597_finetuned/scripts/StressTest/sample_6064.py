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

# the hypothesis refers to the marks obtained by Dacid in various subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in any of the other subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks in English
    # any marks greater than 'english_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
