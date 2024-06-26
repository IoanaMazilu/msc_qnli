# The premise and hypothesis mention the pay rate for Harry
pay_rate_premise = 2
pay_rate_hypothesis = 2

# The premise specifies the number of hours Harry works
first_hours_premise = 30

# The hypothesis specifies the number of hours Harry works
less_than_first_hours_hypothesis = 30

# The hypothesis contradicts the premise by stating that Harry works less than the first hours
if first_hours_premise <= less_than_first_hours_hypothesis:
    # The hypothesis is entailed by the premise, if the number of hours Harry works in the hypothesis is equal to or less than the number of hours in the premise
    label = "entailment"
else:
    # If the number of hours Harry works in the hypothesis is greater than the number of hours in the premise, the hypothesis contradicts the premise
    label = "contradiction"

print(label)
