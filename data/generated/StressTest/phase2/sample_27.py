# Premise: 4200 from Anwar at 6% p.
# Hypothesis: less than 8200 from Anwar at 6% p.
# Golden Label: entailment

amount_premise = 4200
amount_hypothesis = 8200
interest_rate = 6  # same in both premise and hypothesis, no need for separate variables

# the hypothesis refers to an amount taken from Anwar, which is also mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the amount reported in the premise
    label = "contradiction"
elif amount_premise < amount_hypothesis:
    # if the amount in the hypothesis is larger than the one in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise and cannot be explicitly entailed, it is neutral
    label = "neutral"

print(label)

