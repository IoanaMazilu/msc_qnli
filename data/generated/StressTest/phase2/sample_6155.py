# Premise: In 21 years John will be twice as old as Wilson will be then.
# Hypothesis: In 71 years John will be twice as old as Wilson will be then.
# Golden Label: contradiction

john_age_multiplier_premise = 2
wilson_age_multiplier_premise = 1
time_premise = 21

john_age_multiplier_hypothesis = 2
wilson_age_multiplier_hypothesis = 1
time_hypothesis = 71

# The hypothesis talks about the age difference between John and Wilson, referenced also in the premise
if john_age_multiplier_premise != john_age_multiplier_hypothesis or wilson_age_multiplier_premise != wilson_age_multiplier_hypothesis:
    # check if the age multipliers in the hypothesis contradicts the age multipliers in the premise
    label = "contradiction"
elif time_premise != time_hypothesis:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the age multipliers and time periods in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

