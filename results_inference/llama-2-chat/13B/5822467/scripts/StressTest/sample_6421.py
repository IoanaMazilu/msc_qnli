english_marks_premise = 66
english_marks_hypothesis = 76
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
    # if no contradiction, check if the hypothesis values can be explicitly entailed from the premise values
    if english_marks_hypothesis >= english_marks_premise and mathematics_marks_hypothesis >= mathematics_marks_premise and chemistry_marks_hypothesis >= chemistry_marks_premise and biology_marks_hypothesis >= biology_marks_premise and physics_marks_hypothesis >= physics_marks_premise:
        label = "entailment"
    else:
        # if the hypothesis values cannot be explicitly entailed from the premise values, the relation is neutral
        label = "neutral"

print(label)
