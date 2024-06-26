english_marks_premise = 16
english_marks_hypothesis = 96

maths_marks_premise = 95
maths_marks_hypothesis = 95

physics_marks_premise = 82
physics_marks_hypothesis = 82

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87

biology_marks_premise = 92
biology_marks_hypothesis = 92

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
    # if all hypothesis values are consistent with the premise values, we can infer entailment
    label = "entailment"

print(label)
