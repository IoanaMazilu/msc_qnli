premise_passengers = 32300000
premise_year = 1979
hypothesis_passengers = 32300000
hypothesis_year = 1979

# the hypothesis refers to the same year and number of passengers as the premise
if premise_year == hypothesis_year and premise_passengers == hypothesis_passengers:
    # the hypothesis is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"
elif premise_year == hypothesis_year and premise_passengers!= hypothesis_passengers:
    # the hypothesis contradicts the premise, as it mentions a different number of passengers
    label = "contradiction"
else:
    # the hypothesis refers to a different year and/or number of passengers, so it cannot be entailed from the premise
    label = "neutral"

print(label)
