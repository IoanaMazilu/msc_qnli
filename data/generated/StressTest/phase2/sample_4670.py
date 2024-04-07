# Premise: Molly's age in 18 years will be four times her age three years ago.
# Hypothesis: Molly's age in less than 18 years will be four times her age three years ago.
# Golden Label: contradiction

years_future_premise = 18
years_future_hypothesis = 18
years_past = 3
multiplier = 4

# the hypothesis refers to the age calculation mentioned in the premise
if years_future_hypothesis < years_future_premise:
    # check if the 'years_future_hypothesis' contradicts the number of years in the future mentioned in the premise
    label = "contradiction"
else:
    # if the years in the future do not contradict the premise, we cannot infer entailment or contradiction, so the relationship is neutral
    label = "neutral"

print(label)

