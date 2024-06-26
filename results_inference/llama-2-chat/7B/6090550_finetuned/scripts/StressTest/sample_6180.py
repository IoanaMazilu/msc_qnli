english_marks_premise = 86
mathematics_marks_premise = 85
physics_marks_premise = 87
chemistry_marks_premise = 85
biology_marks_premise = 82

english_marks_hypothesis = 16
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 87
chemistry_marks_hypothesis = 85
biology_marks_hypothesis = 82

# the hypothesis refers to the marks obtained by David in each subject, as mentioned in the premise
if english_marks_premise <= english_marks_hypothesis:
    # check if the English marks in the hypothesis contradict the English marks in the premise
    label = "contradiction"
elif mathematics_marks_premise!= mathematics_marks_hypothesis:
    # check if the Mathematics marks in the hypothesis contradict the Mathematics marks in the premise
    label = "contradiction"
elif physics_marks_premise!= physics_marks_hypothesis:
    # check if the Physics marks in the hypothesis contradict the Physics marks in the premise
    label = "contradiction"
elif chemistry_marks_premise!= chemistry_marks_hypothesis:
    # check if the Chemistry marks in the hypothesis contradict the Chemistry marks in the premise
    label = "contradiction"
elif biology_marks_premise!= biology_marks_hypothesis:
    # check if the Biology marks in the hypothesis contradict the Biology marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
