english_marks_premise = 46
english_marks_hypothesis = 86
mathematics_marks_premise = 85
mathematics_marks_hypothesis = 85
physics_marks_premise = 92
physics_marks_hypothesis = 92
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 95
biology_marks_hypothesis = 95

# the hypothesis talks about the marks obtained by Dacid in each subject, referenced also in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradict the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise:
    # check if the marks in Mathematics in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the marks in Physics in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the marks in Chemistry in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks in Biology in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
