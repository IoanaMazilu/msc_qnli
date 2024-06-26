interest_rate_premise = 5
interest_rate_hypothesis = 4

# The hypothesis refers to the interest rate at which Rahul borrowed Rs, also mentioned in the premise
if interest_rate_premise <= interest_rate_hypothesis:
    # Check if the 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
