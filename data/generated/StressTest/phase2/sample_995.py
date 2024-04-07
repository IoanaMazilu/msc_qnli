# Premise: Shankar got 66, 83, 77, 68, 86 marks (out of 100) in English, Maths, physics, Biology and Chemistry.
# Hypothesis: Shankar got less than 66, 83, 77, 68, 86 marks (out of 100) in English, Maths, physics, Biology and Chemistry.
# Golden Label: contradiction

english_marks_premise = 66
maths_marks_premise = 83
physics_marks_premise = 77
biology_marks_premise = 68
chemistry_marks_premise = 86

english_marks_hypothesis = 66
maths_marks_hypothesis = 83
physics_marks_hypothesis = 77
biology_marks_hypothesis = 68
chemistry_marks_hypothesis = 86

# the hypothesis talks about Shankar's marks in 5 subjects, referenced also in the premise
# and hypothesizes that the marks are less than the ones stated in the premise
if english_marks_hypothesis < english_marks_premise or maths_marks_hypothesis < maths_marks_premise or physics_marks_hypothesis < physics_marks_premise or biology_marks_hypothesis < biology_marks_premise or chemistry_marks_hypothesis < chemistry_marks_premise:
    # if the marks in any of the subject hypothesized are less than the marks in premise
    label = "contradiction"
else:
    # the marks in each subject hypothesized are equal to the marks in the premise in each respective subject
    label = "entailment"

print(label)

