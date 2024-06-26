ethnic_slovaks_premise = 100000
ethnic_slovaks_hypothesis = 100000

# the hypothesis talks about the number of Slovaks who have applied to change their citizenship which is also mentioned in the premise
if ethnic_slovaks_hypothesis != ethnic_slovaks_premise:
    # check if the number of Slovaks that applied for citizenship change in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
