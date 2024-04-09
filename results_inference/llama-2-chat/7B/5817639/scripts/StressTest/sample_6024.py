amount_premise = 10000
amount_hypothesis = 6000

# the hypothesis talks about the amount Dana will still owe her parents after 4 years of college
if amount_hypothesis <= amount_premise:
    # check if the hypothesis value contradicts the estimate of 'amount_premise'
    label = "contradiction"
elif amount_hypothesis < 6 * amount_premise / 100:
    # check if the number of months Dana gives back less than 6% of the amount owed contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
