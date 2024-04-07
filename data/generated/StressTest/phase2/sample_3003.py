# Premise: After 2 years, Arun's age will be 26 years.
# Hypothesis: After less than 3 years, Arun's age will be 26 years.
# Golden Label: entailment

arun_future_age_premise = 26
arun_future_years_premise = 2
arun_future_age_hypothesis = 26
arun_future_years_hypothesis = 3

# the hypothesis refers to Arun's future age and time until that age, mentioned in the premise
if arun_future_age_hypothesis != arun_future_age_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
elif arun_future_years_hypothesis <= arun_future_years_premise:
    # check if the time until Arun's future age in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

