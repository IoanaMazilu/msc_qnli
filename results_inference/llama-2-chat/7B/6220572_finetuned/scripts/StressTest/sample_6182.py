english_marks_premise = 86
english_marks_hypothesis = 86
mathematics_marks_premise = 85
mathematics_marks_hypothesis = 85
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained in the subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise:
    # check if the estimate of 'english_marks_hypothesis' contradicts the number of English marks in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis >= mathematics_marks_premise:
    # check if the estimate of'mathematics_marks_hypothesis' contradicts the number of Mathematics marks in the premise
    label = "contradiction"
elif physics_marks_hypothesis >= physics_marks_premise:
    # check if the estimate of 'physics_marks_hypothesis' contradicts the number of Physics marks in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis >= chemistry_marks_premise:
    # check if the estimate of 'chemistry_marks_hypothesis' contradicts the number of Chemistry marks in the premise
    label = "contradiction"
elif biology_marks_hypothesis >= biology_marks_premise:
    # check if the estimate of 'biology_marks_hypothesis' contradicts the number of Biology marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
