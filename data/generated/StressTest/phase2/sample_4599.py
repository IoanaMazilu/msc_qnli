# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 60, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is less than 70, what is his shoe size?
# Golden Label: entailment

life_expectancy_premise = 60
life_expectancy_hypothesis = 70

# the hypothesis talks about Melvin's life expectancy, referenced also in the premise
if life_expectancy_hypothesis <= life_expectancy_premise:
    # check if the hypothesis value contradicts the life expectancy value in the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the life expectancy
    # any life expectancy less than 'life_expectancy_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

