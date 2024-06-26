english_marks_premise = 76
english_marks_hypothesis = 86
maths_marks_premise = 65
maths_marks_hypothesis = 65
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 67
chemistry_marks_hypothesis = 67
biology_marks_premise = 85
biology_marks_hypothesis = 85

# compare the hypothesis values with the premise values
if english_marks_hypothesis < english_marks_premise:
    label = "entailment"
elif maths_marks_hypothesis == maths_marks_premise:
    label = "neutral"
else:
    label = "contradiction"

if physics_marks_hypothesis == physics_marks_premise:
    label = "neutral"
elif chemistry_marks_hypothesis == chemistry_marks_premise:
    label = "neutral"
else:
    label = "contradiction"

if biology_marks_hypothesis == biology_marks_premise:
    label = "neutral"
else:
    label = "contradiction"

print(label)
