cakes_baked_lunch_premise = 5.0
cakes_sold_dinner_premise = 6.0
cakes_baked_yesterday_premise = 3.0
cakes_left_hypothesis = 3.0

# the hypothesis refers to the number of cakes left, which can be computed from the premise
# compute the total number of cakes in the premise
total_cakes_premise = cakes_baked_lunch_premise + cakes_sold_dinner_premise + cakes_baked_yesterday_premise
cakes_left_premise = total_cakes_premise - cakes_sold_dinner_premise

if cakes_left_hypothesis!= cakes_left_premise:
    # check if the number of cakes left in the hypothesis contradicts the number of cakes left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
