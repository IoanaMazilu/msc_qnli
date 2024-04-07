# Premise: Patrick has a lock that contains a less than 7 digit password.
# Hypothesis: Patrick has a lock that contains a 3 digit password.
# Golden Label: neutral

password_digits_premise = 7
password_digits_hypothesis = 3

# the hypothesis refers to the number of digits in Patrick's password mentioned in the premise
if password_digits_hypothesis >= password_digits_premise:
    # check if the hypothesis value contradicts the estimate of less than 'password_digits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of digits
    # any number of digits less than 'password_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

