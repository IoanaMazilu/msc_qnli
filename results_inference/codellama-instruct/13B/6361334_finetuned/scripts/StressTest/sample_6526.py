flights_departed_premise = 3
flights_departed_hypothesis = 60

# the hypothesis refers to the airport's on-time departure rate, which is not mentioned in the premise
if flights_departed_hypothesis <= flights_departed_premise:
    # check if the hypothesis value contradicts the number of flights departed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of flights departed
    # any number of flights greater than 'flights_departed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
