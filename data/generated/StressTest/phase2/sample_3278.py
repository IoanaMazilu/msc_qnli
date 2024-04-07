# Premise: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is 70, what is his shoe size?
# Hypothesis: If Melvin's GMAT score is twice his monthly electric bill, and his life expectancy is less than 70, what is his shoe size?
# Golden Label: contradiction

life_expectancy_premise = 70
life_expectancy_hypothesis = 70

# the hypothesis refers to Melvin's life expectancy mentioned in the premise
if life_expectancy_hypothesis < life_expectancy_premise:
    # check if the life expectancy in the hypothesis contradicts the life expectancy reported in the premise
    label = "contradiction"
else:
    # if the life expectancy in the hypothesis does not contradict the life expectancy in the premise, we can infer entailment
    label = "entailment"

print(label)
