english_marks_premise = 86
math_marks_premise = 89
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 81

english_marks_hypothesis = 56
math_marks_hypothesis = 89
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 81

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_marks_hypothesis!= english_marks_premise:
    # check if the English marks in the hypothesis contradicts the English marks reported in the premise
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise or physics_marks_hypothesis!= physics_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in any other subject in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
