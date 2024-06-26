cakes_baked_premise = 5.0
cakes_sold_premise = 6.0
cakes_baked_yesterday_premise = 3.0
cakes_left_hypothesis = 3.0

# the hypothesis talks about the number of cakes left, which are also referenced in the premise
# compute the total number of cakes baked and sold in the premise
total_cakes_baked_premise = cakes_baked_premise + cakes_baked_yesterday_premise
total_cakes_sold_premise = cakes_sold_premise
# compute the number of cakes left in the hypothesis
cakes_left_premise = total_cakes_baked_premise - total_cakes_sold_premise
if cakes_left_hypothesis!= cakes_left_premise:
    # check if the number of cakes left in the hypothesis contradicts the number of cakes left from the premise
    label = "contradiction"
elif total_cakes_baked_premise!= 8:
    # check if the total number of cakes baked in the premise contradicts the estimate of 8 cakes
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
