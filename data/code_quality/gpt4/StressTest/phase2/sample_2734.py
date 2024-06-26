mohan_beats_sohan_premise = 30
mohan_beats_sohan_hypothesis = 40
sohan_beats_rohan_premise = 80
sohan_beats_rohan_hypothesis = 80

# The hypothesis talks about the distance by which Mohan beats Sohan and Sohan beats Rohan, both also mentioned in the premise
if mohan_beats_sohan_hypothesis <= mohan_beats_sohan_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'mohan_beats_sohan_premise'
    label = "contradiction"
elif sohan_beats_rohan_hypothesis != sohan_beats_rohan_premise:
    # Check if the distance by which Sohan beats Rohan in the hypothesis contradicts the same reported in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the distance by which Mohan beats Sohan
    # Any distance greater than 'mohan_beats_sohan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
