stations_between_delhi_chennai_premise = 85
stations_between_delhi_chennai_hypothesis = 25

# the hypothesis talks about the number of stations between Delhi and Chennai, which is also mentioned in the premise
if stations_between_delhi_chennai_hypothesis >= stations_between_delhi_chennai_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the number of stations in the hypothesis is less than the number of stations in the premise, we can infer entailment
    label = "entailment"

print(label)
