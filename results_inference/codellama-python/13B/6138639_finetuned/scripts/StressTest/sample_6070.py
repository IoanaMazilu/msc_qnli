builder_premise = 1
builder_hypothesis = 2
days_premise = 15
days_hypothesis = 15

# the hypothesis talks about the number of builders and the number of days, referenced also in the premise
if builder_hypothesis <= builder_premise:
    # check if the hypothesis value contradicts the estimate of more than 'builder_premise'
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of builders
    # any number of builders greater than 'builder_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
