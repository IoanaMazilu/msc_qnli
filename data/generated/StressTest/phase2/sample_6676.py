# Premise: Dacid obtained more than 16, 95, 82, 87 and 92 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 96, 95, 82, 87 and 92 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

english_mark_premise = 16
math_mark_premise = 95
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 92

english_mark_hypothesis = 96
math_mark_hypothesis = 95
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 92

# the hypothesis talks about the marks obtained by Dacid in five subjects that are also mentioned in the premise

if english_mark_hypothesis <= english_mark_premise:
    # check if the English mark in the hypothesis contradicts the estimate of more than 'english_mark_premise'
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise or physics_mark_hypothesis != physics_mark_premise or chemistry_mark_hypothesis != chemistry_mark_premise or biology_mark_hypothesis != biology_mark_premise:
    # check if the marks in the hypothesis for other subjects contradict the marks given in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the English mark and exact marks for other subjects
    # the marks provided in the hypothesis are consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

