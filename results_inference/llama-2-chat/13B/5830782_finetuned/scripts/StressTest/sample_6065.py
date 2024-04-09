english_marks_premise = 86
english_marks_hypothesis = 56
math_marks_premise = 89
math_marks_hypothesis = 89
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 81
biology_marks_hypothesis = 81

# the hypothesis talks about the marks obtained by Dacid in various subjects, referenced also in the premise
if english_marks_hypothesis!= english_marks_premise:
    # check if the English marks in the hypothesis contradicts the English marks reported in the premise
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise:
    # check if the Mathematics marks in the hypothesis contradicts the Mathematics marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the Physics marks in the hypothesis contradicts the Physics marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the Chemistry marks in the hypothesis contradicts the Chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the Biology marks in the hypothesis contradicts the Biology marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
