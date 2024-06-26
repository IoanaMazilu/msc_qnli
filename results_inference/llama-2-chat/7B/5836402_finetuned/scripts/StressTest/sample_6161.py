empire_building_height_premise = 356
petronas_towers_height_premise = 370
empire_building_height_hypothesis = 356
petronas_towers_height_hypothesis = 370

# the hypothesis refers to the height difference between the two buildings mentioned in the premise
if empire_building_height_hypothesis >= empire_building_height_premise:
    # check if the hypothesis value contradicts the estimate of less than 'empire_building_height_premise'
    label = "contradiction"
elif petronas_towers_height_hypothesis!= petronas_towers_height_premise:
    # check if the height of the Petronas Towers in the hypothesis contradicts the height of the Petronas Towers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
