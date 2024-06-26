password_digits_premise = 3
password_digits_hypothesis = 7

# the hypothesis refers to the number of digits in the password mentioned in the premise
if password_digits_hypothesis!= password_digits_premise:
    # check if the number of digits in the password in the hypothesis contradicts the number of digits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
