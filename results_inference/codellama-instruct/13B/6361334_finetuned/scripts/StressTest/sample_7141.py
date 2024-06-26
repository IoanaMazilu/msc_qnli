flights_departed_premise = 3
flights_departed_hypothesis = 50

# the hypothesis refers to the number of subsequent flights needed to achieve a higher on-time departure rate than 40%
# the premise mentions the number of flights departed on-time, but does not provide any information about the number of subsequent flights
if flights_departed_hypothesis <= flights_departed_premise:
    # check if the hypothesis value contradicts the number of flights departed on-time in the premise
    label = "contradiction"
else:
    # the premise does not provide any information about the number of subsequent flights needed to achieve a higher on-time departure rate
    # any number of subsequent flights greater than or equal to 'flights_departed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
