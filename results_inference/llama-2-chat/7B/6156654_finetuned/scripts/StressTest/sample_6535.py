# the number of passengers that used Miami Airport in the premise
miami_passengers_premise = 7/3

# the number of passengers that used Miami Airport in the hypothesis
miami_passengers_hypothesis = 1/3

# the number of passengers that used Logan Airport in the premise
logan_passengers_premise = 4 * (miami_passengers_premise - logan_passengers_premise)

# the number of passengers that used Logan Airport in the hypothesis
logan_passengers_hypothesis = 4 * (miami_passengers_hypothesis - logan_passengers_hypothesis)

# check if the number of passengers that used Logan Airport in the hypothesis contradicts the number of passengers that used Logan Airport in the premise
if logan_passengers_hypothesis!= logan_passengers_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
