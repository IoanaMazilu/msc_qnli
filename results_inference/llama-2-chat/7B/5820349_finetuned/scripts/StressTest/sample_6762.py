password_digits_premise = 3
password_digits_hypothesis = 7

# the hypothesis refers to the number of digits in the password mentioned in the premise
if password_digits_premise >= password_digits_hypothesis:
    # check if the number of 'password_digits_premise' contradicts the estimate of less than 'password_digits_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
