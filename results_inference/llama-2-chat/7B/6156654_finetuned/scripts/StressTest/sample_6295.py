percentage_given_to_wife_premise = 60
percentage_given_to_wife_hypothesis = 40

# the hypothesis talks about the percentage of money given to the wife, which is also mentioned in the premise
if percentage_given_to_wife_hypothesis >= percentage_given_to_wife_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is less than the premise value, so it is entailed by the premise
    label = "entailment"

print(label)
