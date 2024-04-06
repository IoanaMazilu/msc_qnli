# Premise: The stolen vehicles were worth more than $1 million.
# Hypothesis: The stolen vehicles were worth more than $1 million, officials said.
# Golden Label: neutral

value_premise = 1000000
value_hypothesis = 1000000

# the hypothesis mentions the worth of the stolen vehicles, which is also mentioned in the premise
# the addition of "officials said" in the hypothesis does not contradict or add information to the numerical entities
if value_hypothesis != value_premise:
    # check if the worth of the vehicles in the hypothesis contradicts the worth reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

