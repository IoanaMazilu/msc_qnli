english_premise = 81
mathematics_premise = 65
physics_premise = 82
chemistry_premise = 67
biology_premise = 85

english_hypothesis = 51
mathematics_hypothesis = 65
physics_hypothesis = 82
chemistry_hypothesis = 67
biology_hypothesis = 85

# the hypothesis refers to the exact marks Dacid obtained in each subject, same as the premise
if english_premise <= english_hypothesis:
    # check if the estimate of 'english_hypothesis' contradicts the number of marks Dacid obtained in English in the premise
    label = "contradiction"
elif mathematics_premise <= mathematics_hypothesis:
    # similarly, we check for Mathematics
    label = "contradiction"
elif physics_premise <= physics_hypothesis:
    # and for Physics
    label = "contradiction"
elif chemistry_premise <= chemistry_hypothesis:
    # and for Chemistry
    label = "contradiction"
elif biology_premise <= biology_hypothesis:
    # and for Biology
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
