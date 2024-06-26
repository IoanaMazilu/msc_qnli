years_future_premise = 7
future_age_premise = 19
years_future_hypothesis = 4
future_age_hypothesis = 19

# Both hypothesis and premise talk about Arun's age in the future
if years_future_premise == years_future_hypothesis and future_age_premise == future_age_hypothesis:
    # If both the number of future years and the future age match in both premise and hypothesis, we can infer entailment
    label = "entailment"
elif years_future_premise != years_future_hypothesis and future_age_premise == future_age_hypothesis:
    # If the number of future years is different but the future age is the same, we have a contradiction
    label = "contradiction"
else:
    # If the number of future years and the future age are both different, the relationship is neutral
    label = "neutral"

print(label)
