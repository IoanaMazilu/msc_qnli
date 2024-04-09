password_length_premise = 3
password_length_hypothesis = 7

# the hypothesis talks about the length of the password in the lock, referenced also in the premise
if password_length_hypothesis <= password_length_premise:
    # check if the hypothesis value contradicts the estimate of more than 'password_length_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the password
    # any length of password greater than 'password_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
