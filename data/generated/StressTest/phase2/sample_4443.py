# Premise: Dacid obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 36, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_marks_premise = 76
mathematics_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 36
mathematics_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in various subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise:
    # check if the hypothesis value contradicts the English marks obtained by Dacid in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis != mathematics_marks_premise:
    # check if the Mathematics marks in the hypothesis contradicts the Mathematics marks obtained by Dacid in the premise
    label = "contradiction"
elif physics_marks_hypothesis != physics_marks_premise:
    # check if the Physics marks in the hypothesis contradicts the Physics marks obtained by Dacid in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis != chemistry_marks_premise:
    # check if the Chemistry marks in the hypothesis contradicts the Chemistry marks obtained by Dacid in the premise
    label = "contradiction"
elif biology_marks_hypothesis != biology_marks_premise:
    # check if the Biology marks in the hypothesis contradicts the Biology marks obtained by Dacid in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

