# Premise: There are less than 50 stations between Trichy and Chennai.
# Hypothesis: There are 10 stations between Trichy and Chennai.
# Golden Label: neutral

stations_premise = 50
stations_hypothesis = 10

# the hypothesis talks about the number of stations between Trichy and Chennai, which is also mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

