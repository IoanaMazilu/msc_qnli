total_distance = 100
traveled_distance = 50

# the hypothesis refers to the number of traveled distance mentioned in the premise
if traveled_distance >= total_distance / 2:
    # check if the estimate of 'traveled_distance' contradicts the number of traveled distance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of traveled distance
    # any number of traveled distance less than 'total_distance / 2' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)