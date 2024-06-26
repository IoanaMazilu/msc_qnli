vikas_rank_premise = 4
vikas_rank_hypothesis = 4
tanvi_rank_premise = 8
tanvi_rank_hypothesis = 8

# the hypothesis refers to the rank of Vikas and Tanvi among the boys and girls in the class
# the premise mentions the rank of Vikas and Tanvi, but does not provide any information about their rank among the girls
if vikas_rank_hypothesis <= vikas_rank_premise:
    # check if the hypothesis value contradicts the estimate of 'vikas_rank_premise'
    label = "contradiction"
elif tanvi_rank_hypothesis!= tanvi_rank_premise:
    # check if the hypothesis value contradicts the estimate of 'tanvi_rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Vikas and Tanvi
    # any rank greater than 'vikas_rank_premise' and 'tanvi_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
