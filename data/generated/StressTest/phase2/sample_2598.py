# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 40, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is more than 30, what is his shoe size?
# Golden Label: entailment

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

