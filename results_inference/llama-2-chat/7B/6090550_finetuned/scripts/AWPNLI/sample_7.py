total_apples_picked_premise = 11.0
total_apples_picked_hypothesis = 10.0

# the hypothesis talks about the total number of apples picked, which is also mentioned in the premise
if total_apples_picked_hypothesis!= total_apples_picked_premise:
    # if the total number of apples picked in the hypothesis does not match with the total number of apples picked in the premise,
    # then the hypothesis contradicts the premise
    label = "contradiction"
else:
    label = "entailment"

print(label)
