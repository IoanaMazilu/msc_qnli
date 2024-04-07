# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 60, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is more than 60, what is his shoe size?
# Golden Label: contradiction

life_expectancy_premise = 60
life_expectancy_hypothesis = 60

# the hypothesis talks about Melvin's life expectancy, referenced also in the premise
if life_expectancy_hypothesis <= life_expectancy_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
else:
    # the premise gives only a specific number for Melvin's life expectancy
    # any number greater than 'life_expectancy_premise' is not consistent with the premise and cannot be explicitly entailed from the premise
    label = "contradiction"

print(label)

