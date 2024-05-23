investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the amount invested by Mr Praveen, also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the amount invested in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)