cars_initial_premise = 50.0
cars_received_premise = 12.0
total_cars_hypothesis = 65.0

# the hypothesis refers to the total number of cars, which is also mentioned in the premise
# compute the total number of cars in the premise
total_cars_premise = cars_initial_premise + cars_received_premise
if total_cars_hypothesis!= total_cars_premise:
    # check if the total number of cars in the hypothesis contradicts the total number of cars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
