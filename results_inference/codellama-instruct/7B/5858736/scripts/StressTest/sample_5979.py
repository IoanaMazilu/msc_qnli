seniors_premise = 300
cars_premise = 150
seniors_hypothesis = 600
cars_hypothesis = 150

# the hypothesis talks about the number of seniors and the percentage of cars owned
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of more than'seniors_premise'
    label = "contradiction"
elif cars_hypothesis <= cars_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cars_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors and the percentage of cars owned
    # any number of seniors and cars greater than the premise estimates is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
