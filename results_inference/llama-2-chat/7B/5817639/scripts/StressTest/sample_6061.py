days_premise = float(input_premise.split("days before the work is finished")[1])
days_hypothesis = float(input_hypothesis.split("days before the work is finished")[1])

# the hypothesis talks about the number of days before the work is finished, referenced also in the premise
if days_hypothesis <= days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days before the work is finished
    # any number of days greater than 'days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
