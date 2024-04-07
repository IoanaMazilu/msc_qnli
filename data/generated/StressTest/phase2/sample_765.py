# Premise: In 4 years, Raj's father age twice as raj, Two years ago, Raj's mother's age twice as raj.
# Hypothesis: In more than 2 years, Raj's father age twice as raj, Two years ago, Raj's mother's age twice as raj.
# Golden Label: entailment

years_future_premise = 4
years_future_hypothesis = 2
years_past_premise = 2
years_past_hypothesis = 2

# the hypothesis refers to the time frames mentioned in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the 'years_future_hypothesis' contradicts the time frame mentioned in the premise
    label = "contradiction"
elif years_past_hypothesis != years_past_premise:
    # check if the 'years_past_hypothesis' contradicts the time frame mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time frames do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

