english_marks_premise = 76
english_marks_hypothesis = 46
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# check if the hypothesis values contradict the premise ones
if english_marks_hypothesis < english_marks_premise:
    label = "contradiction"
elif mathematics_marks_hypothesis == mathematics_marks_premise:
    # no comparison needed, the hypothesis value is consistent with the premise
    label = "neutral"
elif chemistry_marks_hypothesis == chemistry_marks_premise:
    # no comparison needed, the hypothesis value is consistent with the premise
    label = "neutral"
elif biology_marks_hypothesis == biology_marks_premise:
    # no comparison needed, the hypothesis value is consistent with the premise
    label = "neutral"
elif physics_marks_hypothesis == physics_marks_premise:
    # no comparison needed, the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # if none of the above conditions are met, we can infer entailment
    label = "entailment"

print(label)
