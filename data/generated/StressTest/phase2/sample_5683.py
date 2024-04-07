# Premise: more than 2000 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: 6000 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: neutral

total_people_premise = 2000
total_people_hypothesis = 6000

# the hypothesis talks about the number of people (John, Jose & Binoy), which is also referenced in the premise
if total_people_hypothesis <= total_people_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'total_people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

