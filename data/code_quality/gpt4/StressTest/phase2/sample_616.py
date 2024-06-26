tickets_bought_premise = 30
tickets_bought_hypothesis = 10

# the hypothesis talks about the number of concert tickets Martin bought, referenced also in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tickets_bought_premise'
    label = "contradiction"
elif tickets_bought_hypothesis < tickets_bought_premise:
    # the premise gives only an estimate for the number of tickets
    # any number of tickets less than 'tickets_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"
else:
    label = "neutral"

print(label)
