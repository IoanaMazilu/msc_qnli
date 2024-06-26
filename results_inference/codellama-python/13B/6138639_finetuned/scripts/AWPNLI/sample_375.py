baked_cakes_lunch_premise = 5.0
sold_cakes_dinner_premise = 6.0
baked_cakes_yesterday_premise = 3.0
left_cakes_hypothesis = 3.0

# the hypothesis refers to the number of cakes left, which are also mentioned in the premise
# compute the total number of cakes baked in the premise
total_cakes_baked_premise = baked_cakes_lunch_premise + baked_cakes_yesterday_premise
# compute the total number of cakes sold in the premise
total_cakes_sold_premise = sold_cakes_dinner_premise

if left_cakes_hypothesis!= total_cakes_baked_premise - total_cakes_sold_premise:
    # check if the number of cakes left in the hypothesis contradicts the difference between the number of cakes baked and sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
