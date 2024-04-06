# Premise: For hitting a big traffic goal, all 700 or so employees of the viral news site will be getting free Apple smartwatches -- a bonus that will cost at least $245,000.
# Hypothesis: Buzzfeed's 700 employees will get Apple Watches for hitting traffic goals.
# Golden Label: neutral

employees_premise = 700
employees_hypothesis = 700
bonus_cost_premise = 245000

# the hypothesis mentions the number of employees and the reward they will receive (Apple watches), which is also referenced in the premise
if employees_hypothesis != employees_premise:
    # check if the number of employees in the hypothesis contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # if the number of employees in the hypothesis does not contradict the number of employees in the premise, we can infer entailment
    label = "entailment"

print(label)

