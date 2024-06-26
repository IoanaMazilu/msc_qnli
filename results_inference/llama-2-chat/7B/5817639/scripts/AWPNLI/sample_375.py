baked_cakes_premise = 5.0
sold_cakes_premise = 6.0
baked_yesterday_hypothesis = 3.0

# compare the number of cakes baked and sold in the premise and hypothesis
if baked_cakes_premise + sold_cakes_premise!= baked_yesterday_hypothesis:
    # check if the total number of cakes from the hypothesis contradicts the number of cakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
