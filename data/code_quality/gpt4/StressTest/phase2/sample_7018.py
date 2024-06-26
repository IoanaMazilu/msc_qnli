seniors_premise = 800
seniors_hypothesis = 300
car_owners_percentage = 0.4

# the hypothesis talks about the number of seniors at Morse High School, also mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the hypothesis value contradicts the estimate of less than 'seniors_premise'
    label = "contradiction"
elif seniors_hypothesis < seniors_premise:
    # if the hypothesis value is less than the number of seniors in the premise
    # and the percentage of seniors owning cars is consistent with the one in the premise
    # then the hypothesis can be entailed from the premise
    label = "entailment"

print(label)
