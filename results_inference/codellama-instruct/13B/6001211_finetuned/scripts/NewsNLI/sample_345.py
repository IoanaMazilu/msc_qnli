deceased_and_victims_premise = 220000
deceased_and_victims_hypothesis = 220000

# the hypothesis mentions the amount of money each family will receive, which is also mentioned in the premise
if deceased_and_victims_hypothesis!= deceased_and_victims_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis amount does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)
