# Premise: David obtained more than 26, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: neutral

english_marks_premise = 26
maths_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
maths_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# The hypothesis refers to the marks obtained by David in five subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise or maths_marks_hypothesis != maths_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # Check if any of the marks in the hypothesis contradict the marks or estimates in the premise
    label = "contradiction"
else:
    # If the marks in the hypothesis do not contradict the marks or estimates in the premise, we can infer entailment
    label = "entailment"

print(label)

