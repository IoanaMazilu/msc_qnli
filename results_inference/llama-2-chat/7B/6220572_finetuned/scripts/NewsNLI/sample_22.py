poll_states_premise = ["Florida", "Ohio", "Pennsylvania"]
poll_states_hypothesis = ["Ohio", "two other battleground states"]

# the hypothesis mentions the poll states, which are also referenced in the premise
# however, the hypothesis does not provide the exact percentage of Obama's vote in these states, which is mentioned in the premise
# therefore, we cannot infer entailment or contradiction based on this information
label = "neutral"

print(label)
