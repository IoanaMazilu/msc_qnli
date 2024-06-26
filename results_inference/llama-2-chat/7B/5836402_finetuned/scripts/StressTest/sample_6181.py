english_marks_premise = 86
english_marks_hypothesis = 86
mathematics_marks_premise = 85
mathematics_marks_hypothesis = 85
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis talks about the marks obtained by David in different subjects, which are also mentioned in the premise
if english_marks_hypothesis!= english_marks_premise or mathematics_marks_hypothesis!= mathematics_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if any of the marks in the hypothesis contradicts the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
