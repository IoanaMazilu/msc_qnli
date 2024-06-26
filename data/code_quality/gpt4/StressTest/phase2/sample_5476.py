people_voted_premise = 40
people_voted_hypothesis = 10

# the hypothesis refers to the number of people who voted to watch Skip Beat mentioned in the premise
if people_voted_hypothesis >= people_voted_premise:
    # check if the number of people in the hypothesis contradicts the estimate of less than 'people_voted_premise'
    label = "contradiction"
elif people_voted_hypothesis < people_voted_premise:
    # any number of people less than 'people_voted_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)
