# Premise: In a class of boys and girls Vikas's rank is more than 7 th and Tanvi's rank is 17 th.
# Hypothesis: In a class of boys and girls Vikas's rank is 9 th and Tanvi's rank is 17 th.
# Golden Label: neutral

vikas_rank_premise = 7
tanvi_rank_premise = 17
vikas_rank_hypothesis = 9
tanvi_rank_hypothesis = 17

# the hypothesis refers to the ranks of Vikas and Tanvi, mentioned in the premise
if vikas_rank_hypothesis <= vikas_rank_premise:
    # check if 'vikas_rank_hypothesis' contradicts the premise of Vikas's rank being more than 7
    label = "contradiction"
elif tanvi_rank_hypothesis != tanvi_rank_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
elif vikas_rank_hypothesis > vikas_rank_premise and tanvi_rank_hypothesis == tanvi_rank_premise:
    # the premise gives only an estimate for Vikas's rank
    # any rank for Vikas greater than 'vikas_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

