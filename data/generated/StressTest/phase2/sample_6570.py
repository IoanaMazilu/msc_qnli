# Premise: In a class of boys and girls Vikas's rank is 9 th and Tanvi's rank is 17 th.
# Hypothesis: In a class of boys and girls Vikas's rank is more than 7 th and Tanvi's rank is 17 th.
# Golden Label: entailment

vikas_rank_premise = 9
vikas_rank_hypothesis = 7
tanvi_rank_premise = 17
tanvi_rank_hypothesis = 17

# the hypothesis refers to Vikas's and Tanvi's ranks mentioned in the premise
if vikas_rank_premise > vikas_rank_hypothesis:
    # check if the estimate of 'vikas_rank_hypothesis' contradicts Vikas's rank in the premise
    label = "contradiction"
elif tanvi_rank_hypothesis != tanvi_rank_premise:
    # check if the Tanvi's rank in the hypothesis contradicts Tanvi's rank reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

