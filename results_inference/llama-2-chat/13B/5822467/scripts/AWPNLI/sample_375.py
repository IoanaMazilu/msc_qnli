baked_cakes_premise = 5.0
sold_cakes_premise = 6.0
baked_cakes_yesterday = 3.0
left_cakes_hypothesis = 3.0

# compute the total number of cakes baked and sold
total_baked_premise = baked_cakes_premise + baked_cakes_yesterday
total_sold_premise = sold_cakes_premise

# check if the number of left cakes in the hypothesis contradicts the number of baked cakes in the premise
if left_cakes_hypothesis < total_baked_premise:
    label = "contradiction"
elif left_cakes_hypothesis!= total_baked_premise:
    label = "neutral"
else:
    # if the number of left cakes in the hypothesis is consistent with the number of baked cakes in the premise, we can infer entailment
    label = "entailment"

print(label)
