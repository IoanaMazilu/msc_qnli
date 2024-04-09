vikas_rank_premise = 9
vikas_rank_hypothesis = 9
tanvi_rank_premise = 17
tanvi_rank_hypothesis = 17

# the hypothesis talks about the rank of Vikas and Tanvi in their class, which is also mentioned in the premise
if vikas_rank_hypothesis <= vikas_rank_premise:
    # check if the hypothesis value contradicts the premise value of Vikas's rank
    label = "contradiction"
elif tanvi_rank_hypothesis!= tanvi_rank_premise:
    # check if the hypothesis value contradicts the premise value of Tanvi's rank
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
