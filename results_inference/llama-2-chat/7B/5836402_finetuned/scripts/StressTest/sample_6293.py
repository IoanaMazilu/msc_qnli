english_mark_premise = 76
mathematics_mark_premise = 65
chemistry_mark_premise = 82
biology_mark_premise = 67
physics_mark_premise = 85

english_mark_hypothesis = 76
mathematics_mark_hypothesis = 65
chemistry_mark_hypothesis = 82
biology_mark_hypothesis = 67
physics_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in each subject mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the estimate of 'english_mark_hypothesis' contradicts the mark obtained by Arun in English in the premise
    label = "contradiction"
elif mathematics_mark_hypothesis >= mathematics_mark_premise:
    # check if the estimate of'mathematics_mark_hypothesis' contradicts the mark obtained by Arun in Mathematics in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the estimate of 'chemistry_mark_hypothesis' contradicts the mark obtained by Arun in Chemistry in the premise
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the estimate of 'biology_mark_hypothesis' contradicts the mark obtained by Arun in Biology in the premise
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    # check if the estimate of 'physics_mark_hypothesis' contradicts the mark obtained by Arun in Physics in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
