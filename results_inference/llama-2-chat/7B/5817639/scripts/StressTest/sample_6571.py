rank_premise = 7
rank_hypothesis = 9

# the hypothesis talks about the rank of two students, referenced also in the premise
if rank_hypothesis <= rank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of one student
    # any rank greater than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
