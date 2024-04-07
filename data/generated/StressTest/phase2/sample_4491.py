# Premise: Tanya is 25% more efficient than Sakshi.
# Hypothesis: Tanya is less than 45% more efficient than Sakshi.
# Golden Label: entailment

efficiency_tanya_premise = 25
efficiency_tanya_hypothesis = 45

# the hypothesis refers to the efficiency of Tanya compared to Sakshi, mentioned also in the premise
if efficiency_tanya_premise >= efficiency_tanya_hypothesis:
    # check if the increase in efficiency in the hypothesis contradicts the increase in efficiency reported in the premise
    label = "contradiction"
elif efficiency_tanya_premise != efficiency_tanya_hypothesis:
    # check if the increase in efficiency in the hypothesis is exactly the same as in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

