visited_iceland_norway_premise = 41
visited_iceland_norway_hypothesis = 31

# the hypothesis refers to the number of people who visited both Iceland and Norway, which is also mentioned in the premise
if visited_iceland_norway_hypothesis >= visited_iceland_norway_premise:
    # check if the hypothesis value contradicts the estimate of less than 'visited_iceland_norway_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who visited neither country
    # any number of people who visited neither country less than 'visited_iceland_norway_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
