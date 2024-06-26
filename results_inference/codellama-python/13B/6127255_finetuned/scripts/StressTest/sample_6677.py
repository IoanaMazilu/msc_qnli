english_marks_premise = 96
math_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 92

english_marks_hypothesis = 96
math_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 92

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise or math_marks_hypothesis >= math_marks_premise or physics_marks_hypothesis >= physics_marks_premise or chemistry_marks_hypothesis >= chemistry_marks_premise or biology_marks_hypothesis >= biology_marks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
