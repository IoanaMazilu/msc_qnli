english_marks_premise = 86
mathematics_marks_premise = 85
physics_marks_premise = 87
chemistry_marks_premise = 85
biology_marks_premise = 82

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 87
chemistry_marks_hypothesis = 85
biology_marks_hypothesis = 82

# the hypothesis refers to the marks obtained by David in each subject
if english_marks_premise <= english_marks_hypothesis:
    # check if the hypothesis value contradicts the premise value for English marks
    label = "contradiction"
elif mathematics_marks_premise <= mathematics_marks_hypothesis:
    # check if the hypothesis value contradicts the premise value for Mathematics marks
    label = "contradiction"
elif physics_marks_premise <= physics_marks_hypothesis:
    # check if the hypothesis value contradicts the premise value for Physics marks
    label = "contradiction"
elif chemistry_marks_premise <= chemistry_marks_hypothesis:
    # check if the hypothesis value contradicts the premise value for Chemistry marks
    label = "contradiction"
elif biology_marks_premise <= biology_marks_hypothesis:
    # check if the hypothesis value contradicts the premise value for Biology marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
