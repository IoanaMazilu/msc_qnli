# Premise: Standing at 5 feet 7 inches, Clark hit his peak weight at 405 pounds when he was 19.
# Hypothesis: At 405 pounds, Tevante Clark says he was extremely lonely.
# Golden Label: neutral

peak_weight_premise = 405
peak_weight_hypothesis = 405

# the hypothesis mentions the peak weight of the person, which is also mentioned in the premise
if peak_weight_hypothesis != peak_weight_premise:
    # check if the peak weight in the hypothesis contradicts the peak weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

