premise_passengers_total = 32300000
premise_passengers_using_k_airport = 1/3 * premise_passengers_total
premise_passengers_using_k_airport = 1979 * premise_passengers_using_k_airport

hypothesis_passengers_total = 32300000
hypothesis_passengers_using_k_airport = 1/3 * hypothesis_passengers_total
hypothesis_passengers_using_k_airport = 1979 * hypothesis_passengers_using_k_airport

# the hypothesis talks about the number of passengers using Kennedy Airport, referenced also in the premise
if hypothesis_passengers_using_k_airport <= premise_passengers_using_k_airport:
    # check if the hypothesis value contradicts the estimate of more than 'premise_passengers_using_k_airport'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers using Kennedy Airport
    # any number of passengers greater than 'premise_passengers_using_k_airport' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
