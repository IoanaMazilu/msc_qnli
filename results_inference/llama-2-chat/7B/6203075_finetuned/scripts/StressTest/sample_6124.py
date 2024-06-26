group_size_premise = 20
group_size_hypothesis = 60
iceland_visitors_premise = 35
iceland_visitors_hypothesis = 35
norway_visitors_premise = 23
norway_visitors_hypothesis = 23

# the hypothesis talks about the number of people who visited Iceland and Norway, referenced also in the premise
if iceland_visitors_hypothesis!= iceland_visitors_premise:
    # check if the number of people who visited Iceland in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif norway_visitors_hypothesis!= norway_visitors_premise:
    # check if the number of people who visited Norway in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
