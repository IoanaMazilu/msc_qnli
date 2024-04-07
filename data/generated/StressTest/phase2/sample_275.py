# Premise: After 6 years, Arun's age will be 26 years.
# Hypothesis: After less than 6 years, Arun's age will be 26 years.
# Golden Label: contradiction

years_future_premise = 6
years_future_hypothesis = 6
future_age_premise = 26
future_age_hypothesis = 26

# the hypothesis refers to the future age of Arun and the number of years into the future mentioned in the premise
if years_future_premise < years_future_hypothesis:
    # check if the estimate of 'years_future_hypothesis' contradicts the number of future years in the premise
    label = "contradiction"
elif future_age_hypothesis != future_age_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

