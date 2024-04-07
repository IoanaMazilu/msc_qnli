# Premise: David obtained more than 22, 60, 35, 62 and 84 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 72, 60, 35, 62 and 84 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: neutral

english_marks_premise = 22
math_marks_premise = 60
physics_marks_premise = 35
chemistry_marks_premise = 62
biology_marks_premise = 84

english_marks_hypothesis = 72
math_marks_hypothesis = 60
physics_marks_hypothesis = 35
chemistry_marks_hypothesis = 62
biology_marks_hypothesis = 84

# the hypothesis refers to the marks obtained by David in various subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise or math_marks_hypothesis <= math_marks_premise or physics_marks_hypothesis <= physics_marks_premise or chemistry_marks_hypothesis <= chemistry_marks_premise or biology_marks_hypothesis <= biology_marks_premise:
    # check if the marks in the hypothesis contradict the marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

