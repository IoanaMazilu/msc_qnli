# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is less than 800, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 100, what is his shoe size?
# Golden Label: neutral

life_expectancy_premise = 800
life_expectancy_hypothesis = 100

# the hypothesis talks about Melvin's life expectancy, referenced also in the premise
if life_expectancy_hypothesis >= life_expectancy_premise:
    # check if the hypothesis value contradicts the estimate of less than 'life_expectancy_premise'
    label = "contradiction"
elif life_expectancy_hypothesis < life_expectancy_premise:
    # any life expectancy less than 'life_expectancy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

