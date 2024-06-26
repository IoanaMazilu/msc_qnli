life_expectancy_premise = 80
life_expectancy_hypothesis = 80

# the hypothesis talks about the Melvin's life expectancy, referenced also in the premise
if life_expectancy_hypothesis > life_expectancy_premise:
    # check if the hypothesis value contradicts the exact value of 'life_expectancy_premise'
    label = "contradiction"
else:
    # the premise and hypothesis are the same except for "more than" in the hypothesis 
    # since the value is the same, it does not contradict the premise, but cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
