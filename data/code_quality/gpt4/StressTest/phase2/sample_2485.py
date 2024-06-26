english_marks_premise = 86
maths_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
maths_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise or maths_marks_hypothesis > maths_marks_premise or physics_marks_hypothesis > physics_marks_premise or chemistry_marks_hypothesis > chemistry_marks_premise or biology_marks_hypothesis > biology_marks_premise:
    # check if the hypothesis values contradict the premise estimates of less than the respective marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)