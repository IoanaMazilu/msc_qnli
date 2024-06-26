guardsmen_killed_premise = 4
guardsmen_wounded_premise = 80
guardsmen_killed_hypothesis = 4
guardsmen_wounded_hypothesis = 80

# the hypothesis talks about the number of guardsmen killed and wounded in a mortar attack, which is also mentioned in the premise
if guardsmen_killed_hypothesis != guardsmen_killed_premise:
    # check if the number of guardsmen killed in the hypothesis contradicts the number killed in the premise
    label = "contradiction"
elif guardsmen_wounded_hypothesis != guardsmen_wounded_premise:
    # check if the number of guardsmen wounded in the hypothesis contradicts the number wounded in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
