tax_apple_premise = 1
tax_apple_hypothesis = 1

# the hypothesis refers to the tax in apples for each mile towards Bananaville
if tax_apple_hypothesis > tax_apple_premise:
    # check if the tax in the hypothesis contradicts the tax per mile reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
