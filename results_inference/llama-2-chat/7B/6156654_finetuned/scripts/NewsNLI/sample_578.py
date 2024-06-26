# The premise and hypothesis mention the number of peacekeepers to be deployed to a specific country.
# We can infer entailment if the number of peacekeepers in the hypothesis matches the number in the premise.
if 11800 == 11800:
    label = "entailment"
else:
    label = "contradiction"

print(label)
