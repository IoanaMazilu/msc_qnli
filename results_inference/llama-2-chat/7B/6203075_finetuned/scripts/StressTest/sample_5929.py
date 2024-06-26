english_marks_premise = 46
english_marks_hypothesis = 86
math_marks_premise = 85
math_marks_hypothesis = 85
physics_marks_premise = 92
physics_marks_hypothesis = 92
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 95
biology_marks_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in English, Mathematics, Physics, Chemistry and Biology
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradict the English marks in the premise
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in the other subjects in the hypothesis contradict the marks in the same subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis marks do not contradict the premise marks, we can infer entailment
    label = "entailment"

print(label)
