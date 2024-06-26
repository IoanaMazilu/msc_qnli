vikas_rank_top_premise = 4
vikas_rank_bottom_premise = 18
tanvi_rank_top_premise = 8
tanvi_rank_bottom_premise = 21

vikas_rank_top_hypothesis = 4
vikas_rank_bottom_hypothesis = 18
tanvi_rank_top_hypothesis = 8
tanvi_rank_bottom_hypothesis = 21

# the hypothesis refers to the ranks of Vikas and Tanvi mentioned in the premise
if vikas_rank_top_hypothesis <= vikas_rank_top_premise and vikas_rank_bottom_hypothesis == vikas_rank_bottom_premise and tanvi_rank_top_hypothesis == tanvi_rank_top_premise and tanvi_rank_bottom_hypothesis == tanvi_rank_bottom_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif vikas_rank_top_hypothesis > vikas_rank_top_premise and vikas_rank_bottom_hypothesis == vikas_rank_bottom_premise and tanvi_rank_top_hypothesis == tanvi_rank_top_premise and tanvi_rank_bottom_hypothesis == tanvi_rank_bottom_premise:
    # check if the hypothesis values are more than the premise ones
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
