# Premise: Joe had 50.0 toy cars, and he gets 12.0 more cars.
# Hypothesis: He will have 62.0 cars then.
# Golden Label: entailment

initial_cars_premise = 50.0
received_cars_premise = 12.0
total_cars_hypothesis = 62.0

# the hypothesis refers to the total number of cars, which is also calculated in the premise
# compute the total number of cars in the premise
total_cars_premise = initial_cars_premise + received_cars_premise
if total_cars_hypothesis != total_cars_premise:
    # check if the total number of cars in the hypothesis contradicts the total number of cars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

