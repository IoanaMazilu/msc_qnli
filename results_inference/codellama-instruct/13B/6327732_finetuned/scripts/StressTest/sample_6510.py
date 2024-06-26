premise = "If X, Y and Z are digits and 7 XYZ is a 4-digit number that is divisible by 2, which of the following is a possible product of X, Y and Z?"
hypothesis = "If X, Y and Z are digits and more than 5 XYZ is a 4-digit number that is divisible by 2, which of the following is a possible product of X, Y and Z?"

# extract the numerical entities from the premise and hypothesis
premise_digits = [int(s) for s in premise.split() if s.isdigit()]
hypothesis_digits = [int(s) for s in hypothesis.split() if s.isdigit()]

# check if the hypothesis digits are greater than the premise digits
if hypothesis_digits[0] > premise_digits[0]:
    # check if the hypothesis digits are greater than the premise digits
    label = "contradiction"
elif hypothesis_digits[1] > premise_digits[1]:
    # check if the hypothesis digits are greater than the premise digits
    label = "contradiction"
elif hypothesis_digits[2] > premise_digits[2]:
    # check if the hypothesis digits are greater than the premise digits
    label = "contradiction"
else:
    # the hypothesis digits are not greater than the premise digits
    label = "neutral"

print(label)
