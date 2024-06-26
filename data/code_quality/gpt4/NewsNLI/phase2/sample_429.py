toll_violations_premise = 14000
toll_violations_hypothesis = 14000

# the hypothesis mentions the number of toll violations by a vehicle in Texas, which is also mentioned in the premise
if toll_violations_hypothesis == toll_violations_premise:
    # check if the toll violations in the hypothesis match the toll violations reported in the premise
    label = "entailment"
else:
    # if the toll violations in the hypothesis and premise do not match, we can infer contradiction
    label = "contradiction"

print(label)
