# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is more than 10, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 70, what is his shoe size?
# Golden Label: neutral

life_expectancy_premise = 10
life_expectancy_hypothesis = 70

# the hypothesis talks about Melvin's life expectancy which is also mentioned in the premise
if life_expectancy_hypothesis <= life_expectancy_premise:
    # check if the hypothesis value contradicts the estimate of more than 'life_expectancy_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the life expectancy
    # any life expectancy greater than 'life_expectancy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

