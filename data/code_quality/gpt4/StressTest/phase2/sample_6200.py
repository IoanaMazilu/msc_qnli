stations_premise = 18
stations_hypothesis = 88

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis == stations_premise:
    # check if the number of stations in the hypothesis is the same as the number of stations in the premise
    label = "entailment"
elif stations_hypothesis < stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, but also cannot be explicitly entailed from the premise, we infer neutrality
    label = "neutral"

print(label)
