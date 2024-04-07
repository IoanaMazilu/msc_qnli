# Premise: David obtained 86, 85, 82, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained less than 86, 85, 82, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: contradiction

english_mark_premise = 86
mathematics_mark_premise = 85
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 85

english_mark_hypothesis = 86
mathematics_mark_hypothesis = 85
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in the premise
if english_mark_hypothesis >= english_mark_premise or mathematics_mark_hypothesis >= mathematics_mark_premise or physics_mark_hypothesis >= physics_mark_premise or chemistry_mark_hypothesis >= chemistry_mark_premise or biology_mark_hypothesis >= biology_mark_premise:
    # check if the marks in the hypothesis contradict the premise that David obtained less marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, it can be inferred as entailment
    label = "entailment"

print(label)

