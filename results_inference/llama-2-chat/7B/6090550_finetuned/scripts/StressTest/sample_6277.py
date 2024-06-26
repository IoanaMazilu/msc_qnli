ydurbs_banglore_premise = 75
ydurbs_banglore_hypothesis = 15

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, which is also mentioned in the premise
if ydurbs_banglore_hypothesis >= ydurbs_banglore_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
