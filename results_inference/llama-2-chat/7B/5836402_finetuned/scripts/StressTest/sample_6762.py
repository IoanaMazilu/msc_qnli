password_length_premise = 3
password_length_hypothesis = 7

# the hypothesis refers to the length of the password in digits, which is also mentioned in the premise
if password_length_hypothesis >= password_length_premise:
    # check if the hypothesis value contradicts the estimate of less than 'password_length_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
