english_marks_premise = 16
math_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 92

english_marks_hypothesis = 96
math_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 92

# the hypothesis talks about the marks obtained by Dacid in various subjects, referenced also in the premise
if english_marks_hypothesis <= english_marks_premise or math_marks_hypothesis!= math_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the English marks
    # any number of marks greater than 'english_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)