people_iceland_premise = 35
people_norway_premise = 23
people_iceland_hypothesis = 35
people_norway_hypothesis = 23

# the hypothesis talks about the number of people who have visited Iceland and Norway
if people_iceland_hypothesis <= people_iceland_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_iceland_premise'
    label = "contradiction"
elif people_norway_hypothesis <= people_norway_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_norway_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited Iceland and Norway
    # any number of people greater than 'people_iceland_premise' and 'people_norway_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
