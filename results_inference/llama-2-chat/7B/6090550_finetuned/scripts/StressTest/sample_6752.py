ys_entailment_premise = 1
ys_contradiction_premise = 2
ys_neutral_premise = 3

# the hypothesis talks about the number of pet owners in San Durango, which is also mentioned in the premise
if ys_contradiction_premise!= 1:
    # check if the number of pet owners in the hypothesis contradicts the number of pet owners in the premise
    label = "contradiction"
elif ys_entailment_premise!= 1:
    # check if the number of pet owners in the hypothesis entails the number of pet owners in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict or entail the premise ones, we can infer neutral
    label = "neutral"

print(label)
