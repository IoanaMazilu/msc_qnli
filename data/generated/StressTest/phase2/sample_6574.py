# Premise: Vikas's rank among the boys in that class is less than 8 th from the top and 18 th from the bottom and Tanvi's rank among the girls is 8 th from top and 21 st from bottom.
# Hypothesis: Vikas's rank among the boys in that class is 4 th from the top and 18 th from the bottom and Tanvi's rank among the girls is 8 th from top and 21 st from bottom.
# Golden Label: neutral

vikas_rank_top_premise = 8
vikas_rank_bottom_premise = 18
vikas_rank_top_hypothesis = 4
vikas_rank_bottom_hypothesis = 18

tanvi_rank_top_premise = 8
tanvi_rank_bottom_premise = 21
tanvi_rank_top_hypothesis = 8
tanvi_rank_bottom_hypothesis = 21

# the hypothesis refers to the ranks of Vikas and Tanvi which are also mentioned in the premise
if vikas_rank_top_hypothesis >= vikas_rank_top_premise:
    # check if the rank of Vikas from the top in the hypothesis contradicts the rank from the premise
    label = "contradiction"
elif vikas_rank_bottom_hypothesis != vikas_rank_bottom_premise:
    # check if the rank of Vikas from the bottom in the hypothesis contradicts the rank from the premise
    label = "contradiction"
elif tanvi_rank_top_hypothesis != tanvi_rank_top_premise:
    # check if the rank of Tanvi from the top in the hypothesis contradicts the rank from the premise
    label = "contradiction"
elif tanvi_rank_bottom_hypothesis != tanvi_rank_bottom_premise:
    # check if the rank of Tanvi from the bottom in the hypothesis contradicts the rank from the premise
    label = "contradiction"
else:
    # if the ranks of Vikas and Tanvi in the hypothesis do not contradict the ranks in the premise, we can infer entailment
    label = "entailment"

print(label)

