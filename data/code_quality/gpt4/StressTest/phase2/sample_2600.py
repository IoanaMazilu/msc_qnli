life_expectancy_premise = 40
life_expectancy_hypothesis = 10

# The hypothesis talks about Melvin's life expectancy, referenced also in the premise
if life_expectancy_hypothesis != life_expectancy_premise:
    # check if the life expectancy in the hypothesis contradicts the life expectancy reported in the premise
    label = "contradiction"
else:
    # if the life expectancy in the hypothesis does not contradict the life expectancy in the premise, we can infer entailment
    label = "entailment"

print(label)
