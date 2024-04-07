# Premise: Molly's age in 18 years will be four times her age three years ago.
# Hypothesis: Molly's age in less than 58 years will be four times her age three years ago.
# Golden Label: entailment

future_age_premise = 18
future_age_hypothesis = 58
past_age = 3

# the hypothesis talks about Molly's age in the future, and compares it with her age in the past, similarly to the premise
if future_age_hypothesis < future_age_premise:
    # check if the hypothesis future age contradicts the premise future age
    label = "contradiction"
elif future_age_hypothesis == future_age_premise:
    # check if the hypothesis future age explicitly matches the premise future age. 
    # If it does, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis future age does not contradict the premise future age, but also does not match it explicitly,
    # we have a neutral relation
    label = "neutral"

print(label)

