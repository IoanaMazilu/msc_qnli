salesperson_premise = 30
salesperson_hypothesis = 80
shirt_premise = 1
shirt_hypothesis = 1

# the hypothesis refers to the percentage discount for shirts and the purchase of a shirt by Smith, both mentioned in the premise
if salesperson_hypothesis!= salesperson_premise:
    # check if the percentage discount in the hypothesis contradicts the percentage discount reported in the premise
    label = "contradiction"
elif shirt_hypothesis!= shirt_premise:
    # check if the number of shirts bought by Smith in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
