password_premise = 3
password_hypothesis = 7

# the hypothesis refers to the length of the password in the lock
if password_hypothesis <= password_premise:
    # check if the hypothesis value contradicts the estimate of a 3-digit password in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the password
    # any length greater than 3 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
