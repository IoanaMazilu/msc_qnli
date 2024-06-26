baked_cakes_premise_lunch = 5.0
baked_cakes_premise_dinner = 6.0
baked_cakes_yesterday = 3.0
total_cakes = baked_cakes_premise_lunch + baked_cakes_premise_dinner - baked_cakes_yesterday

# the hypothesis refers to the number of cakes left, which can be computed from the premise
# compute the total number of cakes baked and sold
total_cakes_premise = baked_cakes_premise_lunch + baked_cakes_premise_dinner
if total_cakes_premise!= total_cakes:
    # check if the number of cakes left in the hypothesis contradicts the number of cakes left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
