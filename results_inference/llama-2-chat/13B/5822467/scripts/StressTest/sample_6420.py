english_marks_premise = 76
english_marks_hypothesis = 66
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# check if the hypothesis values contradict the premise values
if english_marks_hypothesis < english_marks_premise:
    label = "contradiction"
elif mathematics_marks_hypothesis < mathematics_marks_premise:
    label = "contradiction"
elif chemistry_marks_hypothesis < chemistry_marks_premise:
    label = "contradiction"
elif biology_marks_hypothesis < biology_marks_premise:
    label = "contradiction"
elif physics_marks_hypothesis < physics_marks_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
