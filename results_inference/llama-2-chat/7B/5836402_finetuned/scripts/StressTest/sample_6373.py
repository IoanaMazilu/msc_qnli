pencils_premise = 425
pencils_hypothesis = 125

# the hypothesis refers to the number of pencils Shreehari has, mentioned in the premise
if pencils_hypothesis >= pencils_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pencils_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)
