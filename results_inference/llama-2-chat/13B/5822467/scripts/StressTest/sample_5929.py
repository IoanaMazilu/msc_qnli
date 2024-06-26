english_marks_premise = 46
english_marks_hypothesis = 86

maths_marks_premise = 85
maths_marks_hypothesis = 85

physics_marks_premise = 92
physics_marks_hypothesis = 92

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87

biology_marks_premise = 95
biology_marks_hypothesis = 95

# check if the hypothesis values contradict the premise values
if english_marks_hypothesis!= english_marks_premise:
    label = "contradiction"
elif maths_marks_hypothesis!= maths_marks_premise:
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
