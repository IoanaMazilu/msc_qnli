# Premise: After 6 years, Arun's age will be 26 years.
# Hypothesis: After 3 years, Arun's age will be 26 years.
# Golden Label: contradiction

arun_age_future_premise = 26
arun_future_years_premise = 6
arun_age_future_hypothesis = 26
arun_future_years_hypothesis = 3

# the hypothesis talks about the future age of Arun, mentioned also in the premise
if arun_age_future_premise != arun_age_future_hypothesis:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
elif arun_future_years_premise != arun_future_years_hypothesis:
    # check if the number of years in the future in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

