vikas_rank_premise = 4
vikas_rank_hypothesis = 4
tanvi_rank_premise = 8
tanvi_rank_hypothesis = 8

# the hypothesis refers to the rank of Vikas and Tanvi among the boys and girls in the class
# the premise mentions the rank of Vikas and Tanvi, but does not provide any information about their rank among the girls
if vikas_rank_hypothesis <= vikas_rank_premise:
    # check if the estimate of 'vikas_rank_hypothesis' contradicts the rank of Vikas in the premise
    label = "contradiction"
elif tanvi_rank_hypothesis!= tanvi_rank_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
