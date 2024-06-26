english_marks_premise = 76
english_marks_hypothesis = 76

maths_marks_premise = 65
maths_marks_hypothesis = 65

chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82

biology_marks_premise = 67
biology_marks_hypothesis = 67

physics_marks_premise = 85
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject
if english_marks_premise!= english_marks_hypothesis:
    label = "contradiction"
elif maths_marks_premise!= maths_marks_hypothesis:
    label = "contradiction"
elif chemistry_marks_premise!= chemistry_marks_hypothesis:
    label = "contradiction"
elif biology_marks_premise!= biology_marks_hypothesis:
    label = "contradiction"
elif physics_marks_premise!= physics_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
