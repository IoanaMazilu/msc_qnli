english_mark_premise = 96
mathematics_mark_premise = 95
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 92

english_mark_hypothesis = 96
mathematics_mark_hypothesis = 95
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 92

# the hypothesis refers to the marks obtained by Dacid in each subject, as mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the estimate of 'english_mark_hypothesis' contradicts the mark obtained in English in the premise
    label = "contradiction"
elif mathematics_mark_hypothesis >= mathematics_mark_premise:
    # check if the estimate of'mathematics_mark_hypothesis' contradicts the mark obtained in Mathematics in the premise
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    # check if the estimate of 'physics_mark_hypothesis' contradicts the mark obtained in Physics in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the estimate of 'chemistry_mark_hypothesis' contradicts the mark obtained in Chemistry in the premise
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the estimate of 'biology_mark_hypothesis' contradicts the mark obtained in Biology in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
