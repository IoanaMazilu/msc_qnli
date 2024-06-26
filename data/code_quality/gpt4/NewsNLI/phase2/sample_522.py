destroyed_homes_premise = 11000
damaged_homes_premise = 7000
total_homes_premise = destroyed_homes_premise + damaged_homes_premise

total_homes_hypothesis = 18000

# the hypothesis mentions the total number of homes damaged or destroyed, which is also referenced in the premise
# we compare the total number of homes damaged or destroyed in the premise and hypothesis
if total_homes_hypothesis != total_homes_premise:
    # check if the total number of homes in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
