# the number of passengers that used Miami Airport in the premise
miami_passengers_premise = 1/2 * 1000000

# the number of passengers that used Miami Airport in the hypothesis
miami_passengers_hypothesis = 3/2 * 1000000

# the number of passengers that used Logan Airport in the premise
logan_passengers_premise = 4 * 1000000

# the number of passengers that used Logan Airport in the hypothesis
logan_passengers_hypothesis = 4 * 1000000

# the number of passengers that used Kennedy Airport in the premise
kennedy_passengers_premise = 1/2 * 1000000

# the number of passengers that used Kennedy Airport in the hypothesis
kennedy_passengers_hypothesis = 3/2 * 1000000

# calculate the number of passengers that used Logan Airport in the hypothesis
logan_passengers_hypothesis = logan_passengers_hypothesis * (miami_passengers_hypothesis / kennedy_passengers_hypothesis)

# check if the number of passengers that used Logan Airport in the hypothesis contradicts the number of passengers that used Logan Airport in the premise
if logan_passengers_hypothesis!= logan_passengers_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
