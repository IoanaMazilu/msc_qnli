life_expectancy_premise = 80
life_expectancy_hypothesis = 60

# the hypothesis refers to Melvin's life expectancy mentioned in the premise
if life_expectancy_hypothesis > life_expectancy_premise:
    # check if the estimate of 'life_expectancy_hypothesis' contradicts the life expectancy in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
