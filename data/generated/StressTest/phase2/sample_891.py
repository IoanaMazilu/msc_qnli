# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 100, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is less than 800, what is his shoe size?
# Golden Label: entailment

life_expectancy_premise = 100
life_expectancy_hypothesis = 800

# the hypothesis refers to Melvin's life expectancy mentioned in the premise
if life_expectancy_hypothesis < life_expectancy_premise:
    # check if the 'life_expectancy_hypothesis' contradicts the life expectancy in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

