# Premise: After 5 years, Arun's age will be 25 years.
# Hypothesis: After less than 8 years, Arun's age will be 25 years.
# Golden Label: entailment

arun_future_age_premise = 25
arun_future_age_hypothesis = 25
years_until_future_age_premise = 5
years_until_future_age_hypothesis = 8

# the hypothesis talks about the number of years until Arun reaches a certain age, also mentioned in the premise
if arun_future_age_hypothesis != arun_future_age_premise:
    # check if the future age in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif years_until_future_age_hypothesis < years_until_future_age_premise:
    # check if the number of years until the future age in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

