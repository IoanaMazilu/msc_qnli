english_marks_premise = 76
english_marks_hypothesis = 46
mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65
chemistry_marks_premise = 82
chemistry_marks_hypothesis = 82
biology_marks_premise = 67
biology_marks_hypothesis = 67
physics_marks_premise = 85
physics_marks_hypothesis = 85

# the hypothesis talks about the marks obtained by Arun in each subject, referenced also in the premise
if english_marks_hypothesis!= english_marks_premise:
    # check if the marks obtained in English in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise:
    # check if the marks obtained in Mathematics in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the marks obtained in Chemistry in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks obtained in Biology in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the marks obtained in Physics in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)