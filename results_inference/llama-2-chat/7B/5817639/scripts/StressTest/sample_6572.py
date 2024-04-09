rank_premise = 9
rank_hypothesis = 17

# the hypothesis talks about the ranking of Vikas and Tanvi in a class, mentioned in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis value contradicts the estimate of Vikas's ranking in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Vikas's ranking
    # any ranking greater than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
