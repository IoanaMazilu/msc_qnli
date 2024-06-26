hours_premise = 8
hours_hypothesis = 8
israelis_premise = 25
israelis_hypothesis = 25
palestinians_premise = 25
palestinians_hypothesis = 25

# the hypothesis talks about the number of Israelis and Palestinians who will demonstrate and counter-demonstrate, which are also mentioned in the premise
if israelis_hypothesis!= israelis_premise or palestinians_hypothesis!= palestinians_premise:
    # check if the number of Israelis and Palestinians in the hypothesis contradicts the number of Israelis and Palestinians from the premise
    label = "contradiction"
elif hours_hypothesis!= hours_premise:
    # check if the hours in the hypothesis contradicts the hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
