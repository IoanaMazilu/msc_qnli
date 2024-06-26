home_distance_premise = 50
home_distance_hypothesis = 40
maxwell_speed = 4
brad_speed = 6

# the hypothesis describes a scenario with the same speeds for Maxwell and Brad, but a possibly different home distance
if home_distance_hypothesis >= home_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'home_distance_premise'
    label = "contradiction"
elif home_distance_hypothesis != home_distance_premise:
    # if the home distance in the hypothesis is not equal to the one in the premise, we can't explicitly entail the hypothesis from the premise
    label = "neutral"
else:
    # if the home distances and speeds in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
