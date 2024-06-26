cakes_lunch_premise = 6.0
cakes_dinner_premise = 9.0
more_cakes_hypothesis = 3.0

# the hypothesis refers to the difference in number of cakes served during lunch and dinner, which are also mentioned in the premise
# compute the difference in number of cakes served during lunch and dinner in the premise
difference_cakes_premise = cakes_dinner_premise - cakes_lunch_premise
if more_cakes_hypothesis != difference_cakes_premise:
    # check if the difference in number of cakes in the hypothesis contradicts the difference in number of cakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
