age_dan_premise = 25
age_rob_premise = 26
age_dan_hypothesis = 25
age_rob_hypothesis = 26

# the hypothesis mentions the ages of the victims, which are also mentioned in the premise
# however, the hypothesis does not mention their nationality or occupation, which is mentioned in the premise
if age_dan_hypothesis!= age_dan_premise:
    # check if the age of Dan Parris in the hypothesis contradicts the age of Dan Parris in the premise
    label = "contradiction"
elif age_rob_hypothesis!= age_rob_premise:
    # check if the age of Rob Lehr in the hypothesis contradicts the age of Rob Lehr in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
