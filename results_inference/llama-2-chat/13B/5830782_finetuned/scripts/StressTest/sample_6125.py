group_size_premise = 60
group_size_hypothesis = 40
visited_iceland_premise = 35
visited_iceland_hypothesis = 35
visited_norway_premise = 23
visited_norway_hypothesis = 23

# the hypothesis talks about the size of a group, the number of people who have visited Iceland and Norway
# but the size of the group in the hypothesis is different from the one in the premise
if group_size_hypothesis!= group_size_premise:
    # check if the group size in the hypothesis contradicts the group size in the premise
    label = "contradiction"
elif visited_iceland_hypothesis!= visited_iceland_premise or visited_norway_hypothesis!= visited_norway_premise:
    # check if the number of people who have visited Iceland and Norway in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
