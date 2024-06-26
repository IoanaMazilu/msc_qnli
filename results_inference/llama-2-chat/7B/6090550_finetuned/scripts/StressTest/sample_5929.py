english_marks_premise = 46
mathematics_marks_premise = 85
physics_marks_premise = 92
chemistry_marks_premise = 87
biology_marks_premise = 95

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 95

# the hypothesis talks about the marks obtained by Dacid in different subjects, referenced also in the premise
if english_marks_hypothesis!= english_marks_premise or \
   mathematics_marks_hypothesis!= mathematics_marks_premise or \
   physics_marks_hypothesis!= physics_marks_premise or \
   chemistry_marks_hypothesis!= chemistry_marks_premise or \
   biology_marks_hypothesis!= biology_marks_premise:
    # check if any of the marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
