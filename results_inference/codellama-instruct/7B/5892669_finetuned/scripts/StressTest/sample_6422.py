english_marks_premise = 76
math_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
math_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in different subjects mentioned in the premise
if english_marks_hypothesis!= english_marks_premise:
    # check if the English marks in the hypothesis contradicts the English marks reported in the premise
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise or chemistry_marks_hypothesis!= chemistry_marks_premise or biology_marks_hypothesis!= biology_marks_premise or physics_marks_hypothesis!= physics_marks_premise:
    # check if the marks in any other subject in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)