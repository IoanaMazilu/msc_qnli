english_marks_premise = 51
mathematics_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 81
mathematics_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the exact marks obtained by Dacid in all 5 subjects
if english_marks_hypothesis <= english_marks_premise:
    # check if English marks in the hypothesis contradict the premise
    label = "contradiction"
elif mathematics_marks_hypothesis != mathematics_marks_premise:
    # check if Mathematics marks in the hypothesis contradict the premise
    label = "contradiction"
elif physics_marks_hypothesis != physics_marks_premise:
    # check if Physics marks in the hypothesis contradict the premise
    label = "contradiction"
elif chemistry_marks_hypothesis != chemistry_marks_premise:
    # check if Chemistry marks in the hypothesis contradict the premise
    label = "contradiction"
elif biology_marks_hypothesis != biology_marks_premise:
    # check if Biology marks in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
