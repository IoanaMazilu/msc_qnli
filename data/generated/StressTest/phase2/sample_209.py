# Premise: Dacid obtained 81, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 81, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: contradiction

english_marks_premise = 81
math_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

# the hypothesis refers to the same mark values as the premise, but suggests that they are minimum marks
english_marks_hypothesis = 81
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# compare each pair of corresponding marks in the premise and the hypothesis
if english_marks_premise > english_marks_hypothesis or math_marks_premise > math_marks_hypothesis or physics_marks_premise > physics_marks_hypothesis or chemistry_marks_premise > chemistry_marks_hypothesis or biology_marks_premise > biology_marks_hypothesis:
    # if any mark in the premise is greater than the corresponding mark in the hypothesis, this is a contradiction
    label = "contradiction"
elif english_marks_premise < english_marks_hypothesis or math_marks_premise < math_marks_hypothesis or physics_marks_premise < physics_marks_hypothesis or chemistry_marks_premise < chemistry_marks_hypothesis or biology_marks_premise < biology_marks_hypothesis:
    # if any mark in the premise is less than the corresponding mark in the hypothesis, this is a contradiction
    label = "contradiction"
else:
    # if all marks in the premise are equal to the corresponding marks in the hypothesis, this is a contradiction because the hypothesis suggests that these are minimum marks
    label = "contradiction"

print(label)

