life_expectancy_premise = 70
life_expectancy_hypothesis = 60

# the hypothesis talks about Melvin's life expectancy, referenced also in the premise
if life_expectancy_hypothesis >= life_expectancy_premise:
    # check if the hypothesis value contradicts the estimate of less than 'life_expectancy_premise'
    label = "contradiction"
elif life_expectancy_hypothesis < life_expectancy_premise:
    # the premise gives only an estimate for the life expectancy
    # any life expectancy less than 'life_expectancy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)