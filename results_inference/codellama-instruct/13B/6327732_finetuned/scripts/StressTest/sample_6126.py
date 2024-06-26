people_iceland_premise = 31
people_norway_premise = 31
people_iceland_hypothesis = 41
people_norway_hypothesis = 41

# the hypothesis refers to the number of people who have visited both Iceland and Norway
if people_iceland_hypothesis <= people_iceland_premise and people_norway_hypothesis <= people_norway_premise:
    # check if the hypothesis value contradicts the number of people who have visited both Iceland and Norway in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited both Iceland and Norway
    # any number of people greater than 'people_iceland_premise' and 'people_norway_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
