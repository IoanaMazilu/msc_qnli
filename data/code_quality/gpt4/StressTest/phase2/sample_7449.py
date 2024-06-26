income_percentage_on_petrol_premise = 30
income_percentage_on_petrol_hypothesis = 80

# the hypothesis talks about the percentage of Bhanu's income spent on petrol, which is also referenced in the premise
if income_percentage_on_petrol_hypothesis > income_percentage_on_petrol_premise:
    # check if the hypothesis value contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)