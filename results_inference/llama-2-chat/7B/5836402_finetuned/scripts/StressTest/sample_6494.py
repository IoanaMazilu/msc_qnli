percentage_given_back_premise = 3
percentage_given_back_hypothesis = 3

# the hypothesis refers to the percentage of amount given back to parents, which is also mentioned in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the estimate of 'percentage_given_back_hypothesis' contradicts the percentage of amount given back in the premise
    label = "contradiction"
elif percentage_given_back_hypothesis < percentage_given_back_premise:
    # check if the percentage of amount given back in the hypothesis contradicts the percentage of amount given back in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
