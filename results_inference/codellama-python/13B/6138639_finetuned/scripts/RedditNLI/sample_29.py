homeowners_premise = 5.5
homeowners_hypothesis = 5.5

# the hypothesis and premise mention the number of homeowners by 2010
if homeowners_hypothesis!= homeowners_premise:
    # check if the number of homeowners in the hypothesis contradicts the number of homeowners in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
