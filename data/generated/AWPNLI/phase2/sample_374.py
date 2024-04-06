# Premise: A restaurant baked 5.0 cakes during lunch and sold 6.0 during dinner today and the restaurant baked 3.0 cakes yesterday.
# Hypothesis: 2.0 cakes are left.
# Golden Label: entailment

baked_cakes_lunch_premise = 5.0
sold_cakes_dinner_premise = 6.0
baked_cakes_yesterday_premise = 3.0
left_cakes_hypothesis = 2.0

# the hypothesis refers to the number of cakes left, which can be inferred from the premise
# compute the total number of cakes in the premise
total_cakes_premise = baked_cakes_lunch_premise + baked_cakes_yesterday_premise - sold_cakes_dinner_premise
if left_cakes_hypothesis != total_cakes_premise:
    # check if the number of left cakes in the hypothesis contradicts the number of left cakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

