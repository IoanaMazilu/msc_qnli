cakes_served_premise = 6.0
cakes_returned_premise = 5.0
cakes_successful_yesterday_premise = 3.0
cakes_successful_total_hypothesis = 4.0

# the hypothesis refers to the number of cakes sold successfully, which is also mentioned in the premise
# compute the total number of successful cakes in the premise
cakes_successful_total_premise = (cakes_served_premise - cakes_returned_premise) + cakes_successful_yesterday_premise

if cakes_successful_total_hypothesis != cakes_successful_total_premise:
    # check if the number of successful cakes in the hypothesis contradicts the number of successful cakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
