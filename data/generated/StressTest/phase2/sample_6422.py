# Premise: Arun obtained 76, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Chemistry, Biology and Physics.
# Hypothesis: Arun obtained 46, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Chemistry, Biology and Physics.
# Golden Label: contradiction

english_marks_premise = 76
math_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
math_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the same marks in the same subjects mentioned in the premise
if english_marks_premise != english_marks_hypothesis or math_marks_premise != math_marks_hypothesis or chemistry_marks_premise != chemistry_marks_hypothesis or biology_marks_premise != biology_marks_hypothesis or physics_marks_premise != physics_marks_hypothesis:
    # check if any of the hypothesis marks contradicts the corresponding marks in the premise
    label = "contradiction"
else:
    # if all the hypothesis marks are equal to the corresponding premise marks, we can infer entailment
    label = "entailment"

print(label)

