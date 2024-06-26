initial_cars_premise = 50.0
given_away_cars_premise = 12.0
remaining_cars_hypothesis = 37.0

# the hypothesis refers to the number of remaining cars, which is also mentioned in the premise
# compute the remaining number of cars in the premise
remaining_cars_premise = initial_cars_premise - given_away_cars_premise
if remaining_cars_hypothesis!= remaining_cars_premise:
    # check if the number of remaining cars in the hypothesis contradicts the number of remaining cars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
