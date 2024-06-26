efrida_home = 15
frazer_home = 15
efrida_frazer_distance = 35

# the hypothesis talks about the distance between Efrida and Frazer, referenced also in the premise
if efrida_frazer_distance <= efrida_home + frazer_home:
    # check if the hypothesis value contradicts the estimate of less than 'efrida_frazer_distance'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Efrida and Frazer
    # any number of miles greater than 'efrida_frazer_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
