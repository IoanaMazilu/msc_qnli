premise_empire_state_building = 356
premise_petronas_towers = 370
hypothesis_empire_state_building = 556
hypothesis_petronas_towers = 370

# the hypothesis refers to the height difference between the two buildings
if premise_empire_state_building <= hypothesis_empire_state_building:
    # check if the estimate of 'hypothesis_empire_state_building' contradicts the height of the Empire State Building in the premise
    label = "contradiction"
elif premise_petronas_towers!= hypothesis_petronas_towers:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height of the Petronas Towers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
