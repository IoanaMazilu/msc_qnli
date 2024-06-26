people_lost_power_premise = 125000
people_lost_power_hypothesis = 125000

# the hypothesis mentions the number of people who lost power, which is also mentioned in the premise
if people_lost_power_hypothesis!= people_lost_power_premise:
    # check if the number of people who lost power in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of people who lost power in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
