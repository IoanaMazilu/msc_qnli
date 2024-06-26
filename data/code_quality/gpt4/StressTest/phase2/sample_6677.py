english_marks_premise = 96
english_marks_hypothesis = 96

mathematics_marks_premise = 95
mathematics_marks_hypothesis = 95

physics_marks_premise = 82
physics_marks_hypothesis = 82

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87

biology_marks_premise = 92
biology_marks_hypothesis = 92

# the hypothesis refers to the marks obtained by Dacid in various subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise:
    # check if the english marks in the hypothesis contradict the english marks in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis >= mathematics_marks_premise:
    # check if the mathematics marks in the hypothesis contradict the mathematics marks in the premise
    label = "contradiction"
elif physics_marks_hypothesis >= physics_marks_premise:
    # check if the physics marks in the hypothesis contradict the physics marks in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis >= chemistry_marks_premise:
    # check if the chemistry marks in the hypothesis contradict the chemistry marks in the premise
    label = "contradiction"
elif biology_marks_hypothesis >= biology_marks_premise:
    # check if the biology marks in the hypothesis contradict the biology marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
