# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 20%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 60%?
# Golden Label: neutral

premise_rate = 20
hypothesis_rate = 60

# both hypothesis and premise refer to the airport's on-time departure rate
if premise_rate >= hypothesis_rate:
    # check if the desired on-time departure rate in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any on-time departure rate higher than 'premise_rate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

