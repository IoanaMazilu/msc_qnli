travel_distance_premise = 8800
travel_distance_hypothesis = 1800

# the hypothesis talks about the distance travelled by Rakesh by air, referenced also in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled
    # any distance less than 'travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
