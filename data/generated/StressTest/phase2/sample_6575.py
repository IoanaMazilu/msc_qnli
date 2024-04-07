# Premise: Vikas's rank among the boys in that class is 4 th from the top and 18 th from the bottom and Tanvi's rank among the girls is 8 th from top and 21 st from bottom.
# Hypothesis: Vikas's rank among the boys in that class is more than 4 th from the top and 18 th from the bottom and Tanvi's rank among the girls is 8 th from top and 21 st from bottom.
# Golden Label: contradiction

vikas_rank_top_premise = 4
vikas_rank_bottom_premise = 18
tanvi_rank_top_premise = 8
tanvi_rank_bottom_premise = 21

vikas_rank_top_hypothesis = 4
vikas_rank_bottom_hypothesis = 18
tanvi_rank_top_hypothesis = 8
tanvi_rank_bottom_hypothesis = 21

# the hypothesis talks about Vikas's and Tanvi's rank from the top and bottom, referenced also in the premise
# For Vikas
if vikas_rank_top_hypothesis < vikas_rank_top_premise or vikas_rank_bottom_hypothesis != vikas_rank_bottom_premise:
    # check if the hypothesis values contradict the premise values for Vikas's rank
    label = "contradiction"
# For Tanvi
elif tanvi_rank_top_hypothesis != tanvi_rank_top_premise or tanvi_rank_bottom_hypothesis != tanvi_rank_bottom_premise:
    # check if the hypothesis values contradict the premise values for Tanvi's rank
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

