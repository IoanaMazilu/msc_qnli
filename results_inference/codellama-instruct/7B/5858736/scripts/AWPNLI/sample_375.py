cakes_baked_lunch_premise = 5.0
cakes_sold_dinner_premise = 6.0
cakes_baked_yesterday_premise = 3.0
cakes_left_hypothesis = 3.0

# the hypothesis refers to the number of cakes left, which are also mentioned in the premise
# compute the total number of cakes baked and sold during lunch and dinner
total_cakes_baked_premise = cakes_baked_lunch_premise + cakes_baked_yesterday_premise
total_cakes_sold_premise = cakes_sold_dinner_premise + cakes_baked_yesterday_premise
if cakes_left_hypothesis >= total_cakes_baked_premise:
    # check if the number of cakes left from the hypothesis is greater than or equal to the total number of cakes baked from the premise
    label = "contradiction"
elif cakes_left_hypothesis <= total_cakes_sold_premise:
    # check if the number of cakes left from the hypothesis is less than or equal to the total number of cakes sold from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
