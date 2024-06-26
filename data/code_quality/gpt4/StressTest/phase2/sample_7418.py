future_age_premise = 18
future_age_hypothesis = 18

# Both premise and hypothesis refer to the same calculation involving Molly's age
# The premise specifies that the calculation will be true in 18 years, while the hypothesis suggests it will be true in more than 18 years

if future_age_hypothesis > future_age_premise:
    # the hypothesis proposes a timeline that extends beyond the premise, which does not contradict the premise
    # but it cannot be explicitly entailed from the premise, thus it is neutral
    label = "neutral"
else:
    # if the timeline proposed in the hypothesis does not exceed the premise, it contradicts the premise
    label = "contradiction"

print(label)
