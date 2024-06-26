visited_count_premise = 60
visited_count_hypothesis = 20

# the hypothesis talks about the number of people who have visited Iceland and Norway, referenced also in the premise
if visited_count_hypothesis <= visited_count_premise:
    # check if the hypothesis value contradicts the estimate of more than 'visited_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited Iceland and Norway
    # any number of people who have visited Iceland and Norway greater than 'visited_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
