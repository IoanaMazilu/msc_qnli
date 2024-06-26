visited_iceland_premise = 35
visited_norway_premise = 23
visited_iceland_hypothesis = 35
visited_norway_hypothesis = 23

# the hypothesis talks about the number of people who visited Iceland and Norway, referenced also in the premise
if visited_iceland_hypothesis <= visited_iceland_premise:
    # check if the hypothesis value contradicts the estimate of 'visited_iceland_premise'
    label = "contradiction"
elif visited_norway_hypothesis!= visited_norway_premise:
    # check if the number of people who visited Norway in the hypothesis contradicts the number of people who visited Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
