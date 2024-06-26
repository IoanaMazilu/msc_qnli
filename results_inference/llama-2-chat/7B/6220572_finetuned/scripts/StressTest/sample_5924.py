trip_home_longer_premise = 1/2
trip_home_longer_hypothesis = 4/2

# the hypothesis talks about the longer trip home, referenced also in the premise
if trip_home_longer_hypothesis!= trip_home_longer_premise:
    # check if the hypothesis value contradicts the estimate of 'trip_home_longer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the longer trip home
    # any number of kilometers driven longer than 'trip_home_longer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
