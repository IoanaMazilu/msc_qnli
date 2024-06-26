group_size_premise = 60
group_size_hypothesis = 40
visited_iceland_premise = 35
visited_norway_premise = 23
visited_iceland_hypothesis = 35
visited_norway_hypothesis = 23

# the hypothesis talks about the same group of people as the premise, but with a different size
if group_size_hypothesis!= group_size_premise:
    # check if the number of people visiting Iceland and Norway in the hypothesis contradicts the premise
    if visited_iceland_hypothesis!= visited_iceland_premise or visited_norway_hypothesis!= visited_norway_premise:
        label = "contradiction"
    else:
        # if the hypothesis values do not contradict the premise ones, we can infer entailment
        label = "entailment"
else:
    # if the hypothesis values match the premise ones, we can infer neutrality
    label = "neutral"

print(label)
