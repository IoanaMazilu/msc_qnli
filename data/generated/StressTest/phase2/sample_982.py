# Premise: Dacid obtained more than 42, 45, 72, 77 and 75 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 72, 45, 72, 77 and 75 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

english_mark_premise = 42
math_mark_premise = 45
physics_mark_premise = 72
chemistry_mark_premise = 77
biology_mark_premise = 75

english_mark_hypothesis = 72
math_mark_hypothesis = 45
physics_mark_hypothesis = 72
chemistry_mark_hypothesis = 77
biology_mark_hypothesis = 75

# the hypothesis refers to the exact marks obtained by Dacid in each subject
if english_mark_hypothesis <= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the premise that Dacid obtained more than 42 marks
    label = "contradiction"
elif (math_mark_hypothesis != math_mark_premise or physics_mark_hypothesis != physics_mark_premise or
      chemistry_mark_hypothesis != chemistry_mark_premise or biology_mark_hypothesis != biology_mark_premise):
    # check if the marks in Mathematics, Physics, Chemistry and Biology in the hypothesis contradict the exact marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

