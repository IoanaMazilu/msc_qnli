english_marks_premise = 76
english_marks_hypothesis = 46
math_marks_premise = 65
math_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject as per the premise
if english_marks_hypothesis!= english_marks_premise:
    # check if the English marks in the hypothesis contradict the English marks reported in the premise
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise:
    # check if the Math marks in the hypothesis contradict the Math marks reported in the premise
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
    # if the marks in the hypothesis do not contradict the marks reported in the premise, we can infer entailment
    label = "entailment"

print(label)
