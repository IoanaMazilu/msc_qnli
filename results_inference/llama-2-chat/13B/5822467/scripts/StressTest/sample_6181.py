english_marks_premise = 16
english_marks_hypothesis = 86

maths_marks_premise = 85
maths_marks_hypothesis = 85

physics_marks_premise = 82
physics_marks_hypothesis = 82

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87

biology_marks_premise = 85
biology_marks_hypothesis = 85

# calculate the average marks for each subject
english_avg = (english_marks_premise + english_marks_hypothesis) / 2
maths_avg = (maths_marks_premise + maths_marks_hypothesis) / 2
physics_avg = (physics_marks_premise + physics_marks_hypothesis) / 2
chemistry_avg = (chemistry_marks_premise + chemistry_marks_hypothesis) / 2
biology_avg = (biology_marks_premise + biology_marks_hypothesis) / 2

# compare the average marks
if english_avg == english_marks_hypothesis:
    label = "entailment"
elif english_avg!= english_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

if maths_avg == maths_marks_hypothesis:
    label = "entailment"
elif maths_avg!= maths_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

if physics_avg == physics_marks_hypothesis:
    label = "entailment"
elif physics_avg!= physics_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

if chemistry_avg == chemistry_marks_hypothesis:
    label = "entailment"
elif chemistry_avg!= chemistry_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

if biology_avg == biology_marks_hypothesis:
    label = "entailment"
elif biology_avg!= biology_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
