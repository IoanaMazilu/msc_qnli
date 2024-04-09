people_premise = 7
people_hypothesis = 7
committee_size_premise = 4
committee_size_hypothesis = 4

# the hypothesis talks about the number of people from which a committee is to be selected and the size of the committee, both referenced in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the premise value of 'people_premise'
    label = "contradiction"
elif committee_size_hypothesis!= committee_size_premise:
    # check if the size of the committee in the hypothesis contradicts the size of the committee reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
