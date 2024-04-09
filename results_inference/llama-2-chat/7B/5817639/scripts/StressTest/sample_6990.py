sita_geeta_premise = 2  # number of twins sisters
sita_geeta_hypothesis = 52  # distance run by each twin in opposite directions

# the hypothesis refers to the distance run by each twin in opposite directions, which is less than the premise value
if sita_geeta_hypothesis <= sita_geeta_premise:
    # check if the hypothesis value contradicts the estimate of less than'sita_geeta_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance run,
    # any distance less than'sita_geeta_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
