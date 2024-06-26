english_marks_premise = 16
mathematics_marks_premise = 85
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 85

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 85

# the hypothesis talks about the marks obtained by David in various subjects, which are also referenced in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in any of the subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the English marks
    # any marks greater than 'english_marks_premise' in English is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
