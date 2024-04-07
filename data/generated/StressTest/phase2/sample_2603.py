# Premise: David obtained 36, 35, 42, 57 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 66, 35, 42, 57 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: contradiction

english_marks_premise = 36
math_marks_premise = 35
physics_marks_premise = 42
chemistry_marks_premise = 57
biology_marks_premise = 55

english_marks_hypothesis = 66
math_marks_hypothesis = 35
physics_marks_hypothesis = 42
chemistry_marks_hypothesis = 57
biology_marks_hypothesis = 55

# comparing the marks obtained in individual subjects in the premise and hypothesis
if english_marks_premise != english_marks_hypothesis:
    # check if the English marks in the hypothesis contradicts the English marks in the premise
    label = "contradiction"
elif math_marks_premise != math_marks_hypothesis or physics_marks_premise != physics_marks_hypothesis or chemistry_marks_premise != chemistry_marks_hypothesis or biology_marks_premise != biology_marks_hypothesis:
    # check if the marks in other subjects in the hypothesis contradicts the marks in the same subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

