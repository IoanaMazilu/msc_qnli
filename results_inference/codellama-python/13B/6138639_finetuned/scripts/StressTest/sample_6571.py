vikas_rank_premise = 7
vikas_rank_hypothesis = 9
tanvi_rank_premise = 17
tanvi_rank_hypothesis = 17

# the hypothesis talks about the rank of Vikas and Tanvi in a class, referenced also in the premise
if vikas_rank_hypothesis <= vikas_rank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'vikas_rank_premise'
    label = "contradiction"
elif tanvi_rank_hypothesis!= tanvi_rank_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Vikas
    # any rank of Vikas greater than 'vikas_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
