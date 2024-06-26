english_marks_premise = 16
english_marks_hypothesis = 96
math_marks_premise = 95
math_marks_hypothesis = 95
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 92
biology_marks_hypothesis = 92

# the hypothesis talks about the marks obtained by Dacid in different subjects, which are also mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradict the English marks in the premise
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise:
    # check if the Math marks in the hypothesis contradict the Math marks in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the Physics marks in the hypothesis contradict the Physics marks in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the Chemistry marks in the hypothesis contradict the Chemistry marks in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the Biology marks in the hypothesis contradict the Biology marks in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis do not contradict the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
