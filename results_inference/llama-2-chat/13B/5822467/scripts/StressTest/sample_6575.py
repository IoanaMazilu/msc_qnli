vika_rank_premise = 4
vika_rank_hypothesis = 8
tanvi_rank_premise = 18
tanvi_rank_hypothesis = 21

# the hypothesis refers to the ranks of Vikas and Tanvi in their respective genders and classes
if vika_rank_hypothesis > vika_rank_premise and tanvi_rank_hypothesis > tanvi_rank_premise:
    # the hypothesis is consistent with the premise, no contradiction or entailment can be inferred
    label = "neutral"
elif vika_rank_hypothesis <= vika_rank_premise and tanvi_rank_hypothesis <= tanvi_rank_premise:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"
else:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"

print(label)
