# Premise: In a class of boys and girls Vikas's rank is 9 th and Tanvi's rank is 17 th.
# Hypothesis: In a class of boys and girls Vikas's rank is more than 9 th and Tanvi's rank is 17 th.
# Golden Label: contradiction

vikas_rank_premise = 9
vikas_rank_hypothesis = 9
tanvi_rank_premise = 17
tanvi_rank_hypothesis = 17

# the hypothesis refers to the ranks of Vikas and Tanvi mentioned in the premise
if vikas_rank_hypothesis <= vikas_rank_premise:
    # check if the estimate of 'vikas_rank_hypothesis' contradicts the rank of Vikas in the premise
    label = "contradiction"
elif tanvi_rank_hypothesis != tanvi_rank_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

