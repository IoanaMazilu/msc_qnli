rank_premise = 15
rank_hypothesis = 65
class_size_premise = 47
class_size_hypothesis = 47

# the hypothesis refers to the rank of Nitin in a class of 47 students, mentioned in the premise
if rank_hypothesis <= rank_premise:
    # check if the estimate of 'rank_hypothesis' contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank greater than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
