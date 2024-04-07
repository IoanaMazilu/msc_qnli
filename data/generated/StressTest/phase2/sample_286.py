# Premise: David obtained more than 56, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: neutral

english_marks_premise = 56
math_marks_premise = 65
physics_marks_premise = 82
chem_marks_premise = 67
bio_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chem_marks_hypothesis = 67
bio_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in different subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the number of English marks in the hypothesis contradicts the premise
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or physics_marks_hypothesis != physics_marks_premise or chem_marks_hypothesis != chem_marks_premise or bio_marks_hypothesis != bio_marks_premise:
    # check if the marks in other subjects in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

