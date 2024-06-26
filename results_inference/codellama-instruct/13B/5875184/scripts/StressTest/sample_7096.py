premise_rank = 75
hypothesis_rank = 15

# the hypothesis refers to the rank of Nitin in a class of 47 students
if hypothesis_rank < premise_rank:
    # check if the hypothesis value contradicts the estimate of less than 'premise_rank'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank greater than 'premise_rank' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
