# Premise: After more than 5 years, Arun's age will be 26 years.
# Hypothesis: After 6 years, Arun's age will be 26 years.
# Golden Label: neutral

arun_future_age_premise = 26
arun_future_years_premise = 5
arun_future_age_hypothesis = 26
arun_future_years_hypothesis = 6

# the hypothesis refers to Arun's future age and the number of years in the future mentioned in the premise
if arun_future_age_hypothesis != arun_future_age_premise:
    # check if the future age of Arun in the hypothesis contradicts the future age of Arun in the premise
    label = "contradiction"
elif arun_future_years_hypothesis <= arun_future_years_premise:
    # check if the number of future years in the hypothesis contradicts the number of future years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, it is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"

print(label)

