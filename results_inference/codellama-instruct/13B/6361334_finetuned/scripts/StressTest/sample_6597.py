efrida_frazer_distance_premise = 15
efrida_frazer_distance_hypothesis = 35

# the hypothesis refers to the distance between Efrida and Frazer, mentioned in the premise
if efrida_frazer_distance_hypothesis >= efrida_frazer_distance_premise:
    # check if the hypothesis value contradicts the distance in the premise
    label = "contradiction"
else:
    # the premise gives an exact distance between Efrida and Frazer
    # any distance less than 'efrida_frazer_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
