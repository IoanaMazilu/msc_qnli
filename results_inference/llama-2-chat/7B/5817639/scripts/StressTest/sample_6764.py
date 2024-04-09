password_premise = 3
password_hypothesis = 7

# check if the hypothesis value contradicts the estimate of 'password_premise'
if password_hypothesis > password_premise:
    label = "contradiction"
elif password_hypothesis == password_premise:
    # if the hypothesis value is the same as the estimate, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is less than the estimate, it entails that the password is less than 3 digits
    label = "entailment"

print(label)
