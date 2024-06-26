english_mark_premise = 76
mathematics_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 76
mathematics_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in different subjects, mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the estimate of 'english_mark_hypothesis' contradicts the number of English marks in the premise
    label = "contradiction"
elif mathematics_mark_hypothesis >= mathematics_mark_premise:
    # check if the estimate of'mathematics_mark_hypothesis' contradicts the number of mathematics marks in the premise
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    # check if the estimate of 'physics_mark_hypothesis' contradicts the number of physics marks in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    # check if the estimate of 'chemistry_mark_hypothesis' contradicts the number of chemistry marks in the premise
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    # check if the estimate of 'biology_mark_hypothesis' contradicts the number of biology marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
