# Premise: TANYA IS less than 65% MORE EFFICIENT THAN SAKSHI.
# Hypothesis: TANYA IS 25% MORE EFFICIENT THAN SAKSHI.
# Golden Label: neutral

efficiency_tanya_premise = 65
efficiency_tanya_hypothesis = 25

# the hypothesis refers to the efficiency of Tanya compared to Sakshi, also mentioned in the premise
if efficiency_tanya_hypothesis > efficiency_tanya_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif efficiency_tanya_hypothesis == efficiency_tanya_premise:
    # check if the hypothesis value is equal to the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

