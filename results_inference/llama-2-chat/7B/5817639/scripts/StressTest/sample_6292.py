english_marks_premise = 46
english_marks_hypothesis = 76
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject, as mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the estimate of 'english_marks_hypothesis' contradicts the number of marks obtained in English in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise:
    # check if the number of marks in Mathematics in the hypothesis contradicts the number of marks obtained in Mathematics in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the number of marks in Chemistry in the hypothesis contradicts the number of marks obtained in Chemistry in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the number of marks in Biology in the hypothesis contradicts the number of marks obtained in Biology in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
