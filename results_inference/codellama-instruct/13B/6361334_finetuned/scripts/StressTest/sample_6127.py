people_iceland_premise = 41
people_norway_premise = 41
people_iceland_hypothesis = 31
people_norway_hypothesis = 31

# the hypothesis refers to the number of people who have visited both Iceland and Norway, which is also mentioned in the premise
if people_iceland_hypothesis <= people_iceland_premise and people_norway_hypothesis <= people_norway_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited both Iceland and Norway
    # any number of people greater than 'people_iceland_premise' and 'people_norway_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
