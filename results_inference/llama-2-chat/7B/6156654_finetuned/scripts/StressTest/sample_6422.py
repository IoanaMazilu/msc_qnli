english_marks_premise = 76
english_marks_hypothesis = 46
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# the hypothesis mentions the marks obtained in each subject, which are also mentioned in the premise
if english_marks_hypothesis!= english_marks_premise or mathematics_marks_hypothesis!= mathematics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise or physics_marks_hypothesis!= physics_marks_premise:
    # check if the marks in each subject in the hypothesis contradict the marks in each subject in the premise
    label = "contradiction"
else:
    # if the marks in each subject in the hypothesis do not contradict the marks in each subject in the premise, we can infer entailment
    label = "entailment"

print(label)
