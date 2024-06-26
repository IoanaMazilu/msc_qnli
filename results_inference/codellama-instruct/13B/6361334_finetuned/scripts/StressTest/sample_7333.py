percentage_samsung_premise = 25
percentage_samsung_hypothesis = 75
percentage_iphone_premise = 70
percentage_iphone_hypothesis = 70

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in the same company
if percentage_samsung_hypothesis <= percentage_samsung_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentage_samsung_premise'
    label = "contradiction"
elif percentage_iphone_hypothesis!= percentage_iphone_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
