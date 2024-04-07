# Premise: David obtained less than 86, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: neutral

english_mark_premise = 86
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 76
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis talks about the marks obtained by David in 5 subjects, which are also mentioned in the premise
if english_mark_hypothesis >= english_mark_premise or math_mark_hypothesis >= math_mark_premise or physics_mark_hypothesis >= physics_mark_premise or chemistry_mark_hypothesis >= chemistry_mark_premise or biology_mark_hypothesis >= biology_mark_premise:
    # check if the marks in the hypothesis contradict the premise which states that the marks are less than the given ones
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, then it can be entailed from the premise
    label = "entailment"

print(label)
