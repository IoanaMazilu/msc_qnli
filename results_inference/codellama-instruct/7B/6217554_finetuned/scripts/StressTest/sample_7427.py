english_mark_premise = 76
english_mark_hypothesis = 76
mathematics_mark_premise = 65
mathematics_mark_hypothesis = 65
physics_mark_premise = 82
physics_mark_hypothesis = 82
chemistry_mark_premise = 67
chemistry_mark_hypothesis = 67
biology_mark_premise = 85
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in each subject, referenced also in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the mark obtained in English in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif mathematics_mark_hypothesis >= mathematics_mark_premise:
    # check if the mark obtained in Mathematics in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    # check if the mark obtained in Physics in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the mark obtained in Chemistry in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the mark obtained in Biology in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
