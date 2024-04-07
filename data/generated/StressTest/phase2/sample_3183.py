# Premise: Nitin borrowed some money at the rate of 6% p.
# Hypothesis: Nitin borrowed some money at the rate of more than 2% p.
# Golden Label: entailment

borrowed_rate_premise = 6
borrowed_rate_hypothesis = 2

# The hypothesis speaks about the rate at which Nitin borrowed some money, which is also referenced in the premise.
if borrowed_rate_premise <= borrowed_rate_hypothesis:
    # Check if the hypothesis value contradicts the premise value of 'borrowed_rate_premise'
    label = "contradiction"
elif borrowed_rate_premise > borrowed_rate_hypothesis:
    # If the premise rate is greater than the hypothesis rate, we can infer entailment
    label = "entailment"

print(label)

