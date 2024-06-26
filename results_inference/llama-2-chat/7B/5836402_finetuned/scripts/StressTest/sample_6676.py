english_marks_premise = 16
mathematics_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 92

english_marks_hypothesis = 96
mathematics_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 92

# the hypothesis talks about the marks obtained by Dacid in each subject, which are also referenced in the premise
if english_marks_hypothesis!= english_marks_premise:
    # check if the English marks in the hypothesis contradict the English marks reported in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise:
    # check if the Mathematics marks in the hypothesis contradict the Mathematics marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the Physics marks in the hypothesis contradict the Physics marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the Chemistry marks in the hypothesis contradict the Chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the Biology marks in the hypothesis contradict the Biology marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
