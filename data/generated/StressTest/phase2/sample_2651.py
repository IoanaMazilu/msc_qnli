# Premise: Tanya is 25% more efficient than Sakshi.
# Hypothesis: Tanya is 55% more efficient than Sakshi.
# Golden Label: contradiction

efficiency_tanya_premise = 25
efficiency_tanya_hypothesis = 55

# the hypothesis talks about the efficiency of Tanya compared to Sakshi, which is also mentioned in the premise
if efficiency_tanya_hypothesis == efficiency_tanya_premise:
    # check if the efficiency of Tanya in the hypothesis matches the efficiency mentioned in the premise
    label = "entailment"
elif efficiency_tanya_hypothesis < efficiency_tanya_premise:
    # check if the efficiency of Tanya in the hypothesis contradicts the efficiency mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a certain level of efficiency for Tanya
    # any level of efficiency greater than 'efficiency_tanya_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

