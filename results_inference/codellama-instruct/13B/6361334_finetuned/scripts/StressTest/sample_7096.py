rank_premise = 75
rank_hypothesis = 15

# the hypothesis refers to the rank of Nitin in a class of 47 students, mentioned in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank less than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
