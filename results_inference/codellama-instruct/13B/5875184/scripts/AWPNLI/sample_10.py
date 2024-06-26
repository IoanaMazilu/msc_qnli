premise_lunch = 5.0
premise_dinner = 6.0
premise_yesterday = 3.0
hypothesis = 14.0

# the hypothesis refers to the total number of cakes served, which are also mentioned in the premise
# compute the total number of cakes served in the premise
total_cakes_premise = premise_lunch + premise_dinner + premise_yesterday
if total_cakes_premise!= hypothesis:
    # check if the number of cakes in the hypothesis contradicts the number of cakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
