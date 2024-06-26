produced_cars_NA_premise = 3884.0
recalled_cars_EU_premise = 2871.0
produced_cars_hypothesis = 1013.0

# the hypothesis refers to the number of cars produced, which is also mentioned in the premise
# compute the number of cars successfully produced in the premise
successful_cars_premise = produced_cars_NA_premise - recalled_cars_EU_premise
if produced_cars_hypothesis != successful_cars_premise:
    # check if the number of cars produced in the hypothesis contradicts the number of cars successfully produced from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
