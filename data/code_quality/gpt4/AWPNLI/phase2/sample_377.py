cakes_served_premise = 6.0
cakes_returned_premise = 5.0
cakes_served_yesterday_premise = 3.0
total_cakes_sold_hypothesis = 7.0

# the hypothesis refers to the total number of cakes sold, which is also mentioned in the premise
# compute the total number of cakes sold in the premise
total_cakes_sold_premise = cakes_served_premise - cakes_returned_premise + cakes_served_yesterday_premise
if total_cakes_sold_hypothesis != total_cakes_sold_premise:
    # check if the number of cakes sold in the hypothesis contradicts the number of cakes sold from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
