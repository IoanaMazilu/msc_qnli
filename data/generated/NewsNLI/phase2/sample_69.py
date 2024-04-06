# Premise: The rain-induced floods left nearly 800,000 people displaced, according to the Brazilian civil defense agency.
# Hypothesis: Nation's civil defense agency says nearly 800,000 have been displaced.
# Golden Label: entailment

displaced_people_premise = 800000
displaced_people_hypothesis = 800000

# the hypothesis mentions the number of displaced people, which is also referenced in the premise
# however, the hypothesis does not mention the cause of displacement (rain-induced floods)
# also, the location (Brazil) is not specifically mentioned in the hypothesis

if displaced_people_hypothesis != displaced_people_premise:
    # check if the number of displaced people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of displaced people in the hypothesis does not contradict the number in the premise, we cannot infer entailment but neutrality
    label = "neutral"

print(label)

