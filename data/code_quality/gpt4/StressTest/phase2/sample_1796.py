distance_ran_premise = 6
distance_ran_hypothesis = 8

# the hypothesis talks about the distance ran by two sisters, referenced also in the premise
if distance_ran_hypothesis == distance_ran_premise:
    # check if the hypothesis value matches the distance ran in the premise
    label = "entailment"
elif distance_ran_hypothesis < distance_ran_premise:
    # check if the hypothesis value contradicts the distance ran in the premise
    label = "contradiction"
else:
    # the premise gives the exact distance ran by each sister
    # any distance ran greater than 'distance_ran_premise' contradicts the premise
    label = "contradiction"

print(label)
