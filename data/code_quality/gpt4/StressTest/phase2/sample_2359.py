tip_percentage_john_premise = 75
tip_percentage_john_hypothesis = 15

# the hypothesis talks about the tip percentage John paid over the original price of the dish
if tip_percentage_john_hypothesis >= tip_percentage_john_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tip_percentage_john_premise'
    label = "contradiction"
elif tip_percentage_john_hypothesis > tip_percentage_john_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tip_percentage_john_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
