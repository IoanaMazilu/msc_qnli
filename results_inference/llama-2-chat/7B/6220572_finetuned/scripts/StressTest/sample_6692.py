total_journey_premise = 1800
total_journey_hypothesis = 7800
air_journey_premise = 3/5
air_journey_hypothesis = 3/5

# the hypothesis talks about the number of kilometers travelled by air, referenced also in the premise
if total_journey_hypothesis!= total_journey_premise:
    # check if the total journey in the hypothesis contradicts the total journey reported in the premise
    label = "contradiction"
elif air_journey_hypothesis!= air_journey_premise:
    # check if the proportion of air journey in the hypothesis contradicts the proportion of air journey reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total journey
    # any total journey consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
