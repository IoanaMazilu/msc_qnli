# Premise: Tanya is 20% more efficient than Sakshi.
# Hypothesis: Tanya is more than 20% more efficient than Sakshi.
# Golden Label: contradiction

efficiency_tanya_premise = 20
efficiency_tanya_hypothesis = 20

# the hypothesis talks about the efficiency of Tanya compared to Sakshi, which is also referenced in the premise
if efficiency_tanya_hypothesis <= efficiency_tanya_premise:
    # check if the hypothesis value contradicts the premise value of 'efficiency_tanya_premise'
    label = "contradiction"
else:
    # the premise gives the exact efficiency of Tanya compared to Sakshi
    # any efficiency greater than 'efficiency_tanya_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

