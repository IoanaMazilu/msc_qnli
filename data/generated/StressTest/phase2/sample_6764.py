# Premise: Patrick has a lock that contains a 3 digit password.
# Hypothesis: Patrick has a lock that contains a 7 digit password.
# Golden Label: contradiction

password_digits_premise = 3
password_digits_hypothesis = 7

# the hypothesis refers to the number of digits in Patrick's password lock mentioned in the premise
if password_digits_hypothesis != password_digits_premise:
    # check if the number of digits in the hypothesis contradicts the number of digits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

