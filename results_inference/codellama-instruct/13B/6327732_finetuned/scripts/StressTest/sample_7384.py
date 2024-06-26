class_size_premise = 58
class_size_hypothesis = 58
rank_premise = 74
rank_hypothesis = 24

# the hypothesis refers to the rank of Nitin in a class of 58 students, mentioned in the premise
if rank_premise <= rank_hypothesis:
    # check if the estimate of 'rank_hypothesis' contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank greater than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
