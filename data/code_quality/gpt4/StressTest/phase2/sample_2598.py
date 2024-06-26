life_expectancy_premise = 40
life_expectancy_hypothesis = 30

# The hypothesis refers to Melvin's life expectancy mentioned in the premise
if life_expectancy_premise <= life_expectancy_hypothesis:
    # Check if the estimate of 'life_expectancy_hypothesis' contradicts the life expectancy in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
