speed_premise = 8
speed_hypothesis = 5
meet_distance = 0

# the hypothesis refers to the speed of Fred and Sam, which is consistent with the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of the distance traveled by Sam in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance traveled by Sam, which can be explicitly entailed from the premise
    label = "entailment"
    meet_distance = speed_hypothesis * (speed_premise / 60)
    print(f"Sam has walked {meet_distance} miles when they meet")
