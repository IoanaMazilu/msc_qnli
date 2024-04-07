# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 70, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is more than 10, what is his shoe size?
# Golden Label: entailment

life_expectancy_premise = 70
life_expectancy_hypothesis = 10

# the hypothesis refers to the life expectancy mentioned in the premise
if life_expectancy_premise <= life_expectancy_hypothesis:
    # check if the 'life_expectancy_hypothesis' contradicts the life expectancy in the premise
    label = "contradiction"
else:
    # the premise gives only an exact value for the life expectancy
    # any life expectancy greater than 'life_expectancy_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

