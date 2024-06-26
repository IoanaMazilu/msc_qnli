tax_premise = 300
tax_hypothesis = 300

# the hypothesis refers to the tax added to Harini's pet cost mentioned in the premise
if tax_hypothesis < tax_premise:
    # check if the value of 'tax_hypothesis' contradicts the tax value in the premise
    label = "contradiction"
elif tax_hypothesis > tax_premise:
    # check if the value of 'tax_hypothesis' contradicts the tax value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
