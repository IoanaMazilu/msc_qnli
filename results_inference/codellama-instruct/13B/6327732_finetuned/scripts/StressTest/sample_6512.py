premise = "If X, Y and Z are digits and 7 XYZ is a 4-digit number that is divisible by 2, which of the following is a possible product of X, Y and Z?"
hypothesis = "If X, Y and Z are digits and 3 XYZ is a 4-digit number that is divisible by 2, which of the following is a possible product of X, Y and Z?"

# extract the numerical entities from the premise and hypothesis
premise_digits = [int(s) for s in premise.split() if s.isdigit()]
hypothesis_digits = [int(s) for s in hypothesis.split() if s.isdigit()]

# check if the digits in the hypothesis are the same as the digits in the premise
if premise_digits == hypothesis_digits:
    # if the digits are the same, we can infer entailment
    label = "entailment"
else:
    # if the digits are different, we can infer contradiction
    label = "contradiction"

print(label)
