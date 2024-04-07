# Premise: Tanya is 25% more efficient than Sakshi.
# Hypothesis: Tanya is less than 25% more efficient than Sakshi.
# Golden Label: contradiction

efficiency_premise = 25
efficiency_hypothesis = 25

# the hypothesis talks about the efficiency of Tanya in comparison to Sakshi, which is also referred in the premise
if efficiency_hypothesis < efficiency_premise:
    # check if the hypothesis value contradicts the efficiency of Tanya mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

