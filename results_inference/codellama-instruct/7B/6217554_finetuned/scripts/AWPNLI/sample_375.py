cakes_baked_lunch_premise = 5.0
cakes_sold_dinner_premise = 6.0
cakes_baked_yesterday_premise = 3.0
cakes_left_hypothesis = 3.0

# the hypothesis talks about the number of cakes left, which are also referenced in the premise
# compute the total number of cakes baked and sold from the premise
total_cakes_baked_premise = cakes_baked_lunch_premise + cakes_baked_yesterday_premise
total_cakes_sold_premise = cakes_sold_dinner_premise
if cakes_left_hypothesis!= total_cakes_baked_premise - total_cakes_sold_premise:
    # check if the number of cakes left from the hypothesis contradicts the number of cakes left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
