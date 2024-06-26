vikas_rank_top_premise = 4
vikas_rank_top_hypothesis = 4
vikas_rank_bottom_premise = 18
vikas_rank_bottom_hypothesis = 18
tanvi_rank_top_premise = 8
tanvi_rank_top_hypothesis = 8
tanvi_rank_bottom_premise = 21
tanvi_rank_bottom_hypothesis = 21

# the hypothesis refers to the ranks of Vikas and Tanvi mentioned in the premise
if vikas_rank_top_premise <= vikas_rank_top_hypothesis:
    # check if the estimate of 'vikas_rank_top_hypothesis' contradicts the rank of Vikas in the premise
    label = "contradiction"
elif vikas_rank_bottom_hypothesis!= vikas_rank_bottom_premise:
    # check if the rank of Vikas in the hypothesis contradicts the rank of Vikas reported in the premise
    label = "contradiction"
elif tanvi_rank_top_hypothesis!= tanvi_rank_top_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
elif tanvi_rank_bottom_hypothesis!= tanvi_rank_bottom_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
