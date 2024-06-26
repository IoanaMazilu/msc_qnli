english_mark_premise = 86
mathematics_mark_premise = 85
physics_mark_premise = 92
chemistry_mark_premise = 87
biology_mark_premise = 95

english_mark_hypothesis = 86
mathematics_mark_hypothesis = 85
physics_mark_hypothesis = 92
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in each subject, mentioned in the premise
if english_mark_premise <= english_mark_hypothesis or mathematics_mark_premise <= mathematics_mark_hypothesis or physics_mark_premise <= physics_mark_hypothesis or chemistry_mark_premise <= chemistry_mark_hypothesis or biology_mark_premise <= biology_mark_hypothesis:
    # check if the estimate of 'english_mark_hypothesis','mathematics_mark_hypothesis', 'physics_mark_hypothesis', 'chemistry_mark_hypothesis' or 'biology_mark_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
