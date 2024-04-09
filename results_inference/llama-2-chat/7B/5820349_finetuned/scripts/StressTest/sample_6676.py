english_marks_premise = 16
mathematics_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 92

english_marks_hypothesis = 96
mathematics_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 92

# the hypothesis talks about the marks obtained by Dacid in various subjects, referenced also in the premise
if english_marks_hypothesis <= english_marks_premise or mathematics_marks_hypothesis <= mathematics_marks_premise or physics_marks_hypothesis <= physics_marks_premise or chemistry_marks_hypothesis <= chemistry_marks_premise or biology_marks_hypothesis <= biology_marks_premise:
    # check if the hypothesis values contradict the estimates of more than 'english_marks_premise','mathematics_marks_premise', 'physics_marks_premise', 'chemistry_marks_premise' and 'biology_marks_premise'
    label = "contradiction"
else:
    # the premise gives only estimates for the marks in various subjects
    # any marks greater than 'english_marks_premise','mathematics_marks_premise', 'physics_marks_premise', 'chemistry_marks_premise' and 'biology_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
