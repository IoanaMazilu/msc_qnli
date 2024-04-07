# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 80, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is more than 60, what is his shoe size?
# Golden Label: entailment

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

