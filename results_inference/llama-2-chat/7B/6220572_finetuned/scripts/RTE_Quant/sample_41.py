percentage_return_premise = 5
percentage_return_hypothesis = 5

# the hypothesis talks about the percentage of stolen art that gets returned, which is also mentioned in the premise
if percentage_return_hypothesis!= percentage_return_premise:
    # check if the percentage of stolen art returned in the hypothesis contradicts the percentage from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
