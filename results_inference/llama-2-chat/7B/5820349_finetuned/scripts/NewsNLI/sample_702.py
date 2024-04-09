enemy_view_premise = 0.69
positive_view_hypothesis = 0.12

# the hypothesis mentions the percentage of people who view the US positively, which is not referenced in the premise
# the premise refers to the percentage of people who view the US as an enemy, which is higher than the percentage in the hypothesis
# therefore, we cannot infer entailment or contradiction, but the relationship is neutral
label = "neutral"

print(label)
