english_marks_premise = 96
mathematics_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 97
biology_marks_premise = 95

english_marks_hypothesis = 46
mathematics_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 97
biology_marks_hypothesis = 95

# the hypothesis talks about the marks Dacid obtained in each subject, which were also referenced in the premise
if english_marks_premise <= english_marks_hypothesis or mathematics_marks_premise < mathematics_marks_hypothesis or physics_marks_premise < physics_marks_hypothesis or chemistry_marks_premise < chemistry_marks_hypothesis or biology_marks_premise < biology_marks_hypothesis:
    # check if the hypothesis values contradict the marks Dacid obtained in the premise
    label = "contradiction"
elif english_marks_premise > english_marks_hypothesis:
    # the hypothesis gives an estimate for the English marks which is less than the English marks in the premise
    # any number of English marks greater than 'english_marks_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
