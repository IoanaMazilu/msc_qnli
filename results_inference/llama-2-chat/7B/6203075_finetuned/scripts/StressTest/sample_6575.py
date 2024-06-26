vikas_rank_premise = 4
vikas_rank_top = 18
vikas_rank_bottom = 18
tanvi_rank_premise = 8
tanvi_rank_top = 21
tanvi_rank_bottom = 21

# the hypothesis refers to the same ranks mentioned in the premise
if vikas_rank_premise > 4 or tanvi_rank_premise!= 8:
    # check if the rank of Vikas or Tanvi in the premise contradicts the hypothesis
    label = "contradiction"
elif vikas_rank_top!= 18 or vikas_rank_bottom!= 18:
    # check if the rank of Vikas in the premise contradicts the hypothesis
    label = "contradiction"
elif tanvi_rank_top!= 8 or tanvi_rank_bottom!= 21:
    # check if the rank of Tanvi in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the ranks in the hypothesis do not contradict the ranks in the premise, we can infer entailment
    label = "entailment"

print(label)
