samsung_phone_premise = 0.75
iphone_premise = 0.70
samsung_phone_hypothesis = 0.75
iphone_hypothesis = 0.70

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in the same company
if samsung_phone_hypothesis <= samsung_phone_premise:
    # check if the hypothesis value contradicts the estimate of more than'samsung_phone_premise'
    label = "contradiction"
elif iphone_hypothesis!= iphone_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
