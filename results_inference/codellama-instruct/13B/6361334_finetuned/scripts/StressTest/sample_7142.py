flights_premise = 3
flights_hypothesis = 10

# the hypothesis refers to the number of subsequent flights needed to achieve a higher on-time departure rate
# the premise mentions the number of flights that need to depart on-time for the airport's on-time departure rate to be higher than 50%
if flights_hypothesis <= flights_premise:
    # check if the hypothesis value contradicts the number of flights needed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of flights needed
    # any number of flights greater than 'flights_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
