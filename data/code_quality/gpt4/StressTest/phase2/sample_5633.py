mary_age_difference_premise = 22
mary_age_difference_hypothesis = 72

# the hypothesis talks about the age difference between Mary and Albert, which is also mentioned in the premise
if mary_age_difference_hypothesis == mary_age_difference_premise:
    # check if the age difference in the hypothesis matches the one mentioned in the premise
    label = "entailment"
else:
    # if the age differences do not match, we have a contradiction
    label = "contradiction"

print(label)
