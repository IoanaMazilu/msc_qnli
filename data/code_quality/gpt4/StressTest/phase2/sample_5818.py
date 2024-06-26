people_premise = 8
people_hypothesis = 6

# the hypothesis talks about the number of people Akash will arrange, referenced also in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_premise'
    label = "contradiction"
elif people_hypothesis < people_premise:
    # the premise gives an estimate for the number of people
    # the number of people in the hypothesis is less than 'people_premise' which is consistent with the premise, hence we can infer entailment
    label = "entailment"

print(label)
