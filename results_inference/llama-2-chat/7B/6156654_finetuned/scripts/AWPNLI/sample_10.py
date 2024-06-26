cake_lunch_premise = 5.0
cake_dinner_premise = 6.0
cake_yesterday_premise = 3.0
total_cakes_hypothesis = 14.0

# the hypothesis refers to the total number of cakes served, which can be computed from the premise
# compute the total number of cakes served in the premise
total_cakes_premise = cake_lunch_premise + cake_dinner_premise + cake_yesterday_premise

if total_cakes_hypothesis!= total_cakes_premise:
    # check if the total number of cakes in the hypothesis contradicts the total number of cakes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
