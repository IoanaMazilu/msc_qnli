troops_britain_premise = 4100
troops_us_premise = 142500
troops_britain_hypothesis = 4100
troops_us_hypothesis = 142500

# the hypothesis mentions the number of troops in Iraq for both countries, which are also mentioned in the premise
if troops_britain_hypothesis!= troops_britain_premise:
    # check if the number of troops in Iraq for Britain contradicts the number of troops in the premise
    label = "contradiction"
elif troops_us_hypothesis!= troops_us_premise:
    # check if the number of troops in Iraq for the US contradicts the number of troops in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
