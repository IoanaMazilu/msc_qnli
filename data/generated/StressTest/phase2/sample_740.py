# Premise: Dacid obtained 90, 92, 85, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 60, 92, 85, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: contradiction

english_mark_premise = 90
english_mark_hypothesis = 60
math_mark_premise = 92
math_mark_hypothesis = 92
physics_mark_premise = 85
physics_mark_hypothesis = 85
chemistry_mark_premise = 87
chemistry_mark_hypothesis = 87
biology_mark_premise = 85
biology_mark_hypothesis = 85

# the hypothesis provides the same marks for Mathematics, Physics, Chemistry and Biology as the premise, but a different mark for English
if english_mark_premise != english_mark_hypothesis:
    # check if the English mark in the hypothesis contradicts the English mark in the premise
    label = "contradiction"
elif math_mark_premise != math_mark_hypothesis or physics_mark_premise != physics_mark_hypothesis or chemistry_mark_premise != chemistry_mark_hypothesis or biology_mark_premise != biology_mark_hypothesis:
    # check if any of the other marks in the hypothesis contradict the corresponding marks in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

