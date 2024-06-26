vikas_rank_premise = 7
tanvi_rank_premise = 17
vikas_rank_hypothesis = 9
tanvi_rank_hypothesis = 17

# the hypothesis refers to Vikas's and Tanvi's ranks mentioned in the premise
if vikas_rank_hypothesis <= vikas_rank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'vikas_rank_premise'
    label = "contradiction"
elif tanvi_rank_hypothesis!= tanvi_rank_premise:
    # check if Tanvi's rank in the hypothesis contradicts the rank reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Vikas's rank
    # any rank greater than 'vikas_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
