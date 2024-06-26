english_marks_premise = 86
mathematics_marks_premise = 85
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 85

english_marks_hypothesis = 16
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in each subject mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise:
    # check if the mathematics marks in the hypothesis contradicts the mathematics marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the physics marks in the hypothesis contradicts the physics marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the chemistry marks in the hypothesis contradicts the chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the biology marks in the hypothesis contradicts the biology marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
