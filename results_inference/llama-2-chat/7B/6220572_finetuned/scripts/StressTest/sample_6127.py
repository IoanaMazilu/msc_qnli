visited_norway_premise = 41
visited_norway_hypothesis = 31

# the hypothesis talks about the number of people who have visited both Iceland and Norway, referenced also in the premise
if visited_norway_hypothesis >= visited_norway_premise:
    # check if the hypothesis value contradicts the estimate of less than 'visited_norway_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited both countries
    # any number of people who have visited both countries less than 'visited_norway_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
