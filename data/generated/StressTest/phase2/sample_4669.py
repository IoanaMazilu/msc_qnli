# Premise: Molly's age in less than 58 years will be four times her age three years ago.
# Hypothesis: Molly's age in 18 years will be four times her age three years ago.
# Golden Label: neutral

years_future_premise = 58
years_future_hypothesis = 18
years_past = 3
times_past_age = 4

# The hypothesis refers to Molly's future age, expressed as a multiple of her past age.
# This is the same relationship expressed in the premise, but for a different future time.

if years_future_hypothesis >= years_future_premise:
    # check if the years in the future from the hypothesis contradicts the years in the future from the premise
    label = "contradiction"
elif years_future_hypothesis * times_past_age <= (years_past * times_past_age):
    # check if the relationship between Molly's future and past age contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Molly's future age
    # any future age in less than 'years_future_premise' that is 'times_past_age' times her age 'years_past' ago is consistent with the premise
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

