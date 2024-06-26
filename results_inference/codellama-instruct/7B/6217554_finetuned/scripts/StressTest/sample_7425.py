english_mark_premise = 76
english_mark_hypothesis = 86
math_mark_premise = 65
math_mark_hypothesis = 65
physics_mark_premise = 82
physics_mark_hypothesis = 82
chemistry_mark_premise = 67
chemistry_mark_hypothesis = 67
biology_mark_premise = 85
biology_mark_hypothesis = 85

# the hypothesis talks about the marks obtained by David in each subject, referenced also in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the estimate of 'english_mark_hypothesis' contradicts the English mark obtained in the premise
    label = "contradiction"
elif math_mark_hypothesis!= math_mark_premise:
    # check if the mark obtained in mathematics in the hypothesis contradicts the mark obtained in mathematics in the premise
    label = "contradiction"
elif physics_mark_hypothesis!= physics_mark_premise:
    # check if the mark obtained in physics in the hypothesis contradicts the mark obtained in physics in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis!= chemistry_mark_premise:
    # check if the mark obtained in chemistry in the hypothesis contradicts the mark obtained in chemistry in the premise
    label = "contradiction"
elif biology_mark_hypothesis!= biology_mark_premise:
    # check if the mark obtained in biology in the hypothesis contradicts the mark obtained in biology in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
