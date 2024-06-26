% pylint disable-msg=missing-docstring

premise_variables = {
    "poll_size": 1005,
    "redeem_miles": 40
}

hypothesis_variables = {
    "survey_size": 0,  # not mentioned in the premise
    "redeem_miles_hypothesis": 40  # same value as in the premise
}

# compare the values of the variables in the premise and hypothesis
if premise_variables["redeem_miles"]!= hypothesis_variables["redeem_miles_hypothesis"]:
    # the number of people redeeming miles in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the values of the variables are the same, we can infer entailment
    label = "entailment"

print(label)
