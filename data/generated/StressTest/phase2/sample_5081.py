# Premise: After 6 years, Sandy’s age will be 42 years.
# Hypothesis: After more than 6 years, Sandy’s age will be 42 years.
# Golden Label: contradiction

years_future_premise = 6
years_future_hypothesis = 6
age_future_premise = 42
age_future_hypothesis = 42

# The hypothesis talks about the number of years in the future and Sandy's age at that time, both referenced in the premise
if years_future_hypothesis <= years_future_premise and age_future_hypothesis == age_future_premise:
    # Check if the hypothesis value contradicts the 'years_future_premise' or if the future age contradicts the 'age_future_premise'
    label = "contradiction"
elif age_future_hypothesis != age_future_premise:
    # Check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, then we infer entailment
    label = "entailment"

print(label)

