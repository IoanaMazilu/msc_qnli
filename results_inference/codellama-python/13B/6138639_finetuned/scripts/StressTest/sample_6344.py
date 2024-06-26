discount_premise = 288
discount_hypothesis = 888

# the hypothesis talks about the same discount as the premise, but the value of the discount is different
if discount_hypothesis!= discount_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
