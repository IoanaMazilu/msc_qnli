arun_age_future_premise = 26
arun_age_future_hypothesis = 26
years_future_premise = 6
years_future_hypothesis = 2

# The hypothesis refers to Arun's future age and the number of years mentioned in the premise
if arun_age_future_hypothesis != arun_age_future_premise:
    # Check if the future age of Arun in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif years_future_hypothesis >= years_future_premise:
    # Check if the number of years in the future in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
