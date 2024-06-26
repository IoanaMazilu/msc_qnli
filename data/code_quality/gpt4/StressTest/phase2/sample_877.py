people_arrange_premise = 5
people_arrange_hypothesis = 6

# the hypothesis talks about the number of people Winson will arrange, referenced also in the premise
if people_arrange_hypothesis <= people_arrange_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_arrange_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_arrange_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
