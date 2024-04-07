# Premise: Dacid obtained more than 46, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

english_marks_premise = 46
math_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis provides the exact marks obtained by Dacid in each subject, while the premise only provides an estimate

if english_marks_hypothesis <= english_marks_premise:
    # check if the obtained English marks in the hypothesis contradict the premise
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise:
    # check if the obtained Mathematics marks in the hypothesis contradict the premise
    label = "contradiction"
elif physics_marks_hypothesis != physics_marks_premise:
    # check if the obtained Physics marks in the hypothesis contradict the premise
    label = "contradiction"
elif chemistry_marks_hypothesis != chemistry_marks_premise:
    # check if the obtained Chemistry marks in the hypothesis contradict the premise
    label = "contradiction"
elif biology_marks_hypothesis != biology_marks_premise:
    # check if the obtained Biology marks in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the marks obtained in each subject in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

