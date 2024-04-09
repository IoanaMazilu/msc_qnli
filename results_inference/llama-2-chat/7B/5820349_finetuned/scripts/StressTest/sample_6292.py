english_marks_premise = 46
mathematics_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 76
mathematics_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis talks about the marks Arun obtained in each subject, referenced also in the premise
if english_marks_hypothesis <= english_marks_premise or mathematics_marks_hypothesis <= mathematics_marks_premise or chemistry_marks_hypothesis <= chemistry_marks_premise or biology_marks_hypothesis <= biology_marks_premise or physics_marks_hypothesis <= physics_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_premise' in each subject
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks in each subject
    # any number of marks greater than'marks_premise' in each subject is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
