# Premise: Salley's internet provider offers unlimited traffic which costs $0.5 per day charged off at 12 a.
# Hypothesis: Salley's internet provider offers unlimited traffic which costs $0.5 per day charged off at less than 22 a.
# Golden Label: entailment

charge_time_premise = 12
charge_time_hypothesis = 22

# The hypothesis talks about the time when the internet provider charges for the service, which is also mentioned in the premise
if charge_time_hypothesis < charge_time_premise:
    # check if the hypothesis value contradicts the exact time of 'charge_time_premise'
    label = "contradiction"
elif charge_time_hypothesis > charge_time_premise:
    # any charge time later than 'charge_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

