people_iceland_norway_premise = 31
people_iceland_norway_hypothesis = 41

# the hypothesis refers to the number of people who have visited both Iceland and Norway
# the premise mentions the number of people who have visited neither country
if people_iceland_norway_hypothesis <= people_iceland_norway_premise:
    # check if the hypothesis value contradicts the number of people who have visited both Iceland and Norway in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited neither country
    # any number of people greater than 'people_iceland_norway_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
