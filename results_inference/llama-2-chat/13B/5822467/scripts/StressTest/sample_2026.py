john_age_premise = int(input_premise.split(" ")[1])
john_age_hypothesis = int(input_hypothesis.split(" ")[1])
tom_age_premise = int(input_premise.split(" ")[2])
tom_age_hypothesis = int(input_hypothesis.split(" ")[2])

# check if the estimate of 'john_age_hypothesis' contradicts the number of years ago when John was thrice as old as Tom reported in the premise
if john_age_hypothesis <= john_age_premise:
    label = "contradiction"
elif tom_age_hypothesis!= tom_age_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years ago when John was thrice as old as Tom
    # any number of years greater than the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
