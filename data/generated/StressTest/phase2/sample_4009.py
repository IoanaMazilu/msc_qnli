# Premise: Lindy runs at a constant speed of less than 50 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Hypothesis: Lindy runs at a constant speed of 10 feet per second from Christina to Jack, back to Christina, back to Jack, and so forth.
# Golden Label: neutral

speed_premise = 50
speed_hypothesis = 10

# the hypothesis talks about Lindy's running speed, referenced also in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'speed_premise'
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # the premise gives only an estimate for the speed
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

