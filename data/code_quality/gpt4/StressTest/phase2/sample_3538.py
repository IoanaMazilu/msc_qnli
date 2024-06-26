returned_tshirts_premise = 6
returned_tshirts_hypothesis = 3

# the hypothesis talks about the number of t-shirts returned by Sanoop, also mentioned in the premise
if returned_tshirts_hypothesis >= returned_tshirts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'returned_tshirts_premise'
    label = "contradiction"
elif returned_tshirts_hypothesis < returned_tshirts_premise:
    # if the number of returned t-shirts in the hypothesis is less than the number in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
