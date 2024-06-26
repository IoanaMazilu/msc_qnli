watermelons_premise = 700
watermelons_hypothesis = 200

# the hypothesis refers to the number of watermelons Mike had, which is also mentioned in the premise
if watermelons_hypothesis >= watermelons_premise:
    # check if the hypothesis value contradicts the estimate of less than 'watermelons_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
