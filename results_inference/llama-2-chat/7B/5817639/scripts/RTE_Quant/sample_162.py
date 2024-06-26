fda_pills_premise = 70e6
fda_pills_hypothesis = 200

# the hypothesis talks about the number of pills with metal detected by the FDA, which is also mentioned in the premise
if fda_pills_hypothesis!= fda_pills_premise:
    # check if the number of pills with metal detected in the hypothesis contradicts the number of pills from the premise
    label = "contradiction"
elif fda_pills_hypothesis > fda_pills_premise:
    # check if the number of pills with metal detected in the hypothesis is greater than the number of pills from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
