english_marks_premise = 76
math_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in different subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise:
    # check if the estimate of 'english_marks_hypothesis' contradicts the number of English marks in the premise
    label = "contradiction"
elif math_marks_hypothesis!= math_marks_premise:
    # check if the number of Math marks in the hypothesis contradicts the number of Math marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the number of Physics marks in the hypothesis contradicts the number of Physics marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the number of Chemistry marks in the hypothesis contradicts the number of Chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the number of Biology marks in the hypothesis contradicts the number of Biology marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
