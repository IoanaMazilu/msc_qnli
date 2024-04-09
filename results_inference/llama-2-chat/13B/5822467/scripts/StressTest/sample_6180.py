english_marks_premise = 86
english_marks_hypothesis = 16

maths_marks_premise = 85
maths_marks_hypothesis = 85

physics_marks_premise = 82
physics_marks_hypothesis = 87

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 85

biology_marks_premise = 85
biology_marks_hypothesis = 85

# calculate the averages for each subject
english_avg = english_marks_premise / 5
maths_avg = maths_marks_premise / 5
physics_avg = physics_marks_premise / 5
chemistry_avg = chemistry_marks_premise / 5
biology_avg = biology_marks_premise / 5

# compare the hypothesized marks with the premise marks
if english_avg <= english_marks_hypothesis:
    label = "contradiction"
elif maths_avg!= maths_marks_hypothesis:
    label = "contradiction"
elif physics_avg!= physics_marks_hypothesis:
    label = "contradiction"
elif chemistry_avg!= chemistry_marks_hypothesis:
    label = "contradiction"
elif biology_avg!= biology_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
