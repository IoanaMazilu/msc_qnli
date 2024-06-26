english_marks_premise = 76
maths_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
maths_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in different subjects, mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the estimate of English marks in the hypothesis contradicts the English marks reported in the premise
    label = "contradiction"
elif maths_marks_hypothesis!= maths_marks_premise:
    # check if the estimate of Maths marks in the hypothesis contradicts the Maths marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the estimate of Chemistry marks in the hypothesis contradicts the Chemistry marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the estimate of Biology marks in the hypothesis contradicts the Biology marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the estimate of Physics marks in the hypothesis contradicts the Physics marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
