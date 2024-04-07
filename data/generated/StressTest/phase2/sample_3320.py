# Premise: After 4 years, Arun's age will be 32 years.
# Hypothesis: After less than 4 years, Arun's age will be 32 years.
# Golden Label: contradiction

years_future_premise = 4
years_future_hypothesis = 4
age_future_premise = 32
age_future_hypothesis = 32

# the hypothesis refers to the same time frame and same age as the premise
if years_future_hypothesis >= years_future_premise:
    # check if the hypothesis contradicts the premise about the number of years in the future
    label = "contradiction"
elif age_future_hypothesis != age_future_premise:
    # check if the future age in the hypothesis contradicts the future age in the premise
    label = "contradiction"
else:
    # if the hypothesis time frame and future age do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

