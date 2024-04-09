passenger_count_premise = float(7)/3
passenger_count_hypothesis = 1/3

# the hypothesis talks about the number of passengers using Logan Airport, referenced also in the premise
if passenger_count_hypothesis <= passenger_count_premise:
    # check if the hypothesis value contradicts the estimate of 'passenger_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers using Logan Airport
    # any number of passengers using Logan Airport consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
