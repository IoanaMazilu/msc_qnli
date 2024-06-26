southward_distance_premise = 60
southward_distance_hypothesis = 20

# the hypothesis talks about the distance Raviraj cycled southwards, which is also mentioned in the premise
if southward_distance_hypothesis >= southward_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'southward_distance_premise'
    label = "contradiction"
elif southward_distance_hypothesis < southward_distance_premise:
    # the premise gives only an upper limit for the southward distance
    # any distance less than 'southward_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
