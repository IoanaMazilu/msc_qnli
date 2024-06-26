english_marks_premise = 66
english_marks_hypothesis = 76
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject mentioned in the premise
if english_marks_premise!= english_marks_hypothesis:
    # check if the English marks in the hypothesis contradict the English marks reported in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise:
    # check if the Mathematics marks in the hypothesis contradict the Mathematics marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the Chemistry marks in the hypothesis contradict the Chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the Biology marks in the hypothesis contradict the Biology marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the Physics marks in the hypothesis contradict the Physics marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
