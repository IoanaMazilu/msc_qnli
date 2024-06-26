english_marks_premise = 86
english_marks_hypothesis = 56
mathematics_marks_premise = 89
mathematics_marks_hypothesis = 89
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 81
biology_marks_hypothesis = 81

# the hypothesis talks about the marks obtained by Dacid in each subject, referenced also in the premise
if english_marks_hypothesis!= english_marks_premise:
    # check if the marks obtained in English in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis!= mathematics_marks_premise:
    # check if the marks obtained in Mathematics in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis!= physics_marks_premise:
    # check if the marks obtained in Physics in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis!= chemistry_marks_premise:
    # check if the marks obtained in Chemistry in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the marks obtained in Biology in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
