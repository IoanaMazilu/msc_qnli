english_marks_premise = 16
mathematics_marks_premise = 85
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 85

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 85

# the hypothesis talks about the marks obtained by David in different subjects, which is also mentioned in the premise
if english_marks_premise!= english_marks_hypothesis:
    # check if the english marks in the hypothesis contradicts the english marks in the premise
    label = "contradiction"
elif mathematics_marks_premise!= mathematics_marks_hypothesis:
    # check if the mathematics marks in the hypothesis contradicts the mathematics marks in the premise
    label = "contradiction"
elif physics_marks_premise!= physics_marks_hypothesis:
    # check if the physics marks in the hypothesis contradicts the physics marks in the premise
    label = "contradiction"
elif chemistry_marks_premise!= chemistry_marks_hypothesis:
    # check if the chemistry marks in the hypothesis contradicts the chemistry marks in the premise
    label = "contradiction"
elif biology_marks_premise!= biology_marks_hypothesis:
    # check if the biology marks in the hypothesis contradicts the biology marks in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis do not contradict the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
