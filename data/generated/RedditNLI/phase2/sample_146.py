# Premise: China cuts interest rates for third time in six months as economy sputters.
# Hypothesis: China adds stimulus with third rate cut in six months.
# Golden Label: entailment

cuts_premise = 3
cuts_hypothesis = 3
months_premise = 6
months_hypothesis = 6

# the hypothesis and premise mention the number of rate cuts and the time period over which they occurred
if cuts_premise != cuts_hypothesis:
    # check if the number of rate cuts in the hypothesis contradicts the number of rate cuts in the premise
    label = "contradiction"
elif months_hypothesis != months_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

