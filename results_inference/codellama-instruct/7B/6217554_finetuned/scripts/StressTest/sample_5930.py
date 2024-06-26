english_mark_premise = 86
english_mark_hypothesis = 86
mathematics_mark_premise = 85
mathematics_mark_hypothesis = 85
physics_mark_premise = 92
physics_mark_hypothesis = 92
chemistry_mark_premise = 87
chemistry_mark_hypothesis = 87
biology_mark_premise = 95
biology_mark_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in each subject, mentioned in the premise
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
