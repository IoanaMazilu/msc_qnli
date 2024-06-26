english_marks_premise = 86
english_marks_hypothesis = 56
mathematics_marks_premise = 89
mathematics_marks_hypothesis = 89
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 81
biology_marks_hypothesis = 81

# the hypothesis refers to the marks obtained by Dacid in English, Mathematics, Physics, Chemistry and Biology
if english_marks_hypothesis!= english_marks_premise or \
   mathematics_marks_hypothesis!= mathematics_marks_premise or \
   physics_marks_hypothesis!= physics_marks_premise or \
   chemistry_marks_hypothesis!= chemistry_marks_premise or \
   biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis marks do not contradict the premise marks, we can infer entailment
    label = "entailment"

print(label)
