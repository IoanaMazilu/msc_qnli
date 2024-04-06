# Premise: A restaurant baked 5.0 cakes during lunch and sold 6.0 during dinner today and the restaurant baked 3.0 cakes yesterday.
# Hypothesis: 3.0 cakes are left.
# Golden Label: contradiction

baked_cakes_lunch_premise = 5.0
sold_cakes_dinner_premise = 6.0
baked_cakes_yesterday_premise = 3.0
left_cakes_hypothesis = 3.0

# the hypothesis refers to the number of cakes left, which can be estimated from the premise
# compute the total number of baked cakes and sold cakes
total_baked_cakes_premise = baked_cakes_lunch_premise + baked_cakes_yesterday_premise
total_sold_cakes_premise = sold_cakes_dinner_premise

# compute the number of cakes left in the premise
left_cakes_premise = total_baked_cakes_premise - total_sold_cakes_premise

if left_cakes_hypothesis != left_cakes_premise:
    # check if the number of cakes left in the hypothesis contradicts the number of cakes left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

