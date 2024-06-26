english_marks_premise = 16
math_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 92

english_marks_hypothesis = 96
math_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 92

# the hypothesis refers to the marks obtained by Dacid in each subject, which are also mentioned in the premise
if english_marks_hypothesis!= english_marks_premise or math_marks_hypothesis!= math_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
