password_length_premise = 3
password_length_hypothesis = 7

# the hypothesis talks about the length of the password, referenced also in the premise
if password_length_hypothesis!= password_length_premise:
    # check if the length of the password in the hypothesis contradicts the length of the password reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact length of the password
    # the hypothesis value does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
