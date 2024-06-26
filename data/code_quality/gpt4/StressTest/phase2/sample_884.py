stations_premise = 28
stations_hypothesis = 28

# the hypothesis talks about the number of stations between Ernakulam and Chennai, mentioned also in the premise
if stations_hypothesis != stations_premise:
    # check if the hypothesis value contradicts the exact number of stations in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of stations. 
    # the exact number of stations can be explicitly entailed from the premise
    label = "entailment"

print(label)
