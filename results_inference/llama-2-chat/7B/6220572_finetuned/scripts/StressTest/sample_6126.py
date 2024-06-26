people_iceland_norway_premise = 31
people_iceland_norway_hypothesis = 41

# the hypothesis talks about the number of people who visited both Iceland and Norway, referenced also in the premise
if people_iceland_norway_hypothesis <= people_iceland_norway_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_iceland_norway_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who visited both countries
    # any number of people less than 'people_iceland_norway_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
