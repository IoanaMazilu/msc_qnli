english_marks_premise = 76
math_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
math_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in different subjects, mentioned in the premise
if english_marks_premise <= english_marks_hypothesis:
    # check if the estimate of 'english_marks_hypothesis' contradicts the number of English marks in the premise
    label = "contradiction"
elif math_marks_premise!= math_marks_hypothesis:
    # check if the number of Math marks in the hypothesis contradicts the number of Math marks reported in the premise
    label = "contradiction"
elif chemistry_marks_premise!= chemistry_marks_hypothesis:
    # check if the number of Chemistry marks in the hypothesis contradicts the number of Chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_premise!= biology_marks_hypothesis:
    # check if the number of Biology marks in the hypothesis contradicts the number of Biology marks reported in the premise
    label = "contradiction"
elif physics_marks_premise!= physics_marks_hypothesis:
    # check if the number of Physics marks in the hypothesis contradicts the number of Physics marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)