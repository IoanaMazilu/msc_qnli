english_marks_premise = 76
maths_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 76
maths_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject, which are also mentioned in the premise
if english_marks_hypothesis >= english_marks_premise or maths_marks_hypothesis >= maths_marks_premise or chemistry_marks_hypothesis >= chemistry_marks_premise or biology_marks_hypothesis >= biology_marks_premise or physics_marks_hypothesis >= physics_marks_premise:
    # if the hypothesis values are greater than or equal to the premise ones, it contradicts the hypothesis statement of obtaining less marks
    label = "contradiction"
else:
    # if the hypothesis values are less than the premise ones, it is consistent with the hypothesis statement of obtaining less marks
    label = "entailment"

print(label)
