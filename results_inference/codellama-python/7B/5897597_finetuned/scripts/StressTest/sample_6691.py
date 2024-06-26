kilometres_travelled_premise = 8800
kilometres_travelled_hypothesis = 1800

# the hypothesis talks about the distance travelled by air, referenced also in the premise
if kilometres_travelled_hypothesis >= kilometres_travelled_premise:
    # check if the hypothesis value contradicts the estimate of less than 'kilometres_travelled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled by air
    # any distance less than 'kilometres_travelled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
