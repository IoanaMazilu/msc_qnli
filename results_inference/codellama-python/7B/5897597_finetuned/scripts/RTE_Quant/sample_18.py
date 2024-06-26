total_killed_premise = 70000
displaced_premise = 2000000
killed_hypothesis = 200000

# the hypothesis talks about the number of people killed in the Darfur region, which is also mentioned in the premise
if killed_hypothesis > total_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the total number of people killed in the premise
    label = "contradiction"
elif killed_hypothesis < total_killed_premise:
    # check if the number of people killed in the hypothesis is less than the total number of people killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
