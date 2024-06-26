english_mark_premise = 61
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 51
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis specifies the marks Dacid got in several subjects, which are also mentioned in the premise
if english_mark_premise <= english_mark_hypothesis:
    # check if the estimate of 'english_mark_hypothesis' contradicts the English mark in the premise
    label = "contradiction"
elif math_mark_premise <= math_mark_hypothesis:
    # check if the estimate of 'math_mark_hypothesis' contradicts the Math mark in the premise
    label = "contradiction"
elif physics_mark_premise <= physics_mark_hypothesis:
    # check if the estimate of 'physics_mark_hypothesis' contradicts the Physics mark in the premise
    label = "contradiction"
elif chemistry_mark_premise <= chemistry_mark_hypothesis:
    # check if the estimate of 'chemistry_mark_hypothesis' contradicts the Chemistry mark in the premise
    label = "contradiction"
elif biology_mark_premise <= biology_mark_hypothesis:
    # check if the estimate of 'biology_mark_hypothesis' contradicts the Biology mark in the premise
    label = "contradiction"
else:
    # if all the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
