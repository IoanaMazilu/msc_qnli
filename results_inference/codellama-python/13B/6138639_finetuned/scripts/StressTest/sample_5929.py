english_marks_premise = 46
math_marks_premise = 85
physics_marks_premise = 92
chemistry_marks_premise = 87
biology_marks_premise = 95

english_marks_hypothesis = 86
math_marks_hypothesis = 85
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 95

# the hypothesis talks about the marks obtained by Dacid in different subjects, referenced also in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks obtained in the other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained in English
    # any number of marks greater than 'english_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
