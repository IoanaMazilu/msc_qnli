vikas_rank_premise = 4
vikas_rank_top = 18
vikas_rank_bottom = 18
tanvi_rank_premise = 8
tanvi_rank_top = 21
tanvi_rank_bottom = 21

# the hypothesis mentions the rank of Vikas and Tanvi in the class, which are also mentioned in the premise
if vikas_rank_premise!= vikas_rank_top:
    # check if the rank of Vikas in the premise contradicts the rank in the hypothesis
    label = "contradiction"
elif vikas_rank_bottom!= vikas_rank_bottom:
    # check if the rank of Vikas in the premise contradicts the rank in the hypothesis
    label = "contradiction"
elif tanvi_rank_premise!= tanvi_rank_top:
    # check if the rank of Tanvi in the premise contradicts the rank in the hypothesis
    label = "contradiction"
elif tanvi_rank_bottom!= tanvi_rank_bottom:
    # check if the rank of Tanvi in the premise contradicts the rank in the hypothesis
    label = "contradiction"
else:
    # if the ranks in the premise and hypothesis do not contradict, we can infer entailment
    label = "entailment"

print(label)
