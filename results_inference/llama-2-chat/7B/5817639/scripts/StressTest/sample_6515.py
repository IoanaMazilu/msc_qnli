old_john_premise = 3 * 6 = 18
old_john_hypothesis = 3 * 2 = 6

# the hypothesis talks about John's age at a different time than the premise
if old_john_hypothesis <= old_john_premise:
    # check if the hypothesis value contradicts the estimate of John's age in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for John's age at a different time than the hypothesis
    # any number of years that John was older than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
