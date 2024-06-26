dan_parris_age_premise = 25
rob_lehr_age_premise = 26
dan_parris_age_hypothesis = 25
rob_lehr_age_hypothesis = 26

# the hypothesis mentions the ages of the two victims, which are also mentioned in the premise
if dan_parris_age_hypothesis!= dan_parris_age_premise:
    # check if the age of Dan Parris in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif rob_lehr_age_hypothesis!= rob_lehr_age_premise:
    # check if the age of Rob Lehr from the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the ages in the hypothesis do not contradict the ages in the premise, we can infer entailment
    label = "entailment"

print(label)
