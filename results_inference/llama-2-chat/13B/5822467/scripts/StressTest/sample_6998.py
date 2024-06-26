sacha_speed_premise = 9
bruno_speed_premise = 5
sacha_speed_hypothesis = float(input("Enter Sacha's speed (in meters per second): "))
bruno_speed_hypothesis = float(input("Enter Bruno's speed (in meters per second): "))

# Check if Sacha's speed in the hypothesis is more than the speed in the premise
if sacha_speed_hypothesis > sacha_speed_premise:
    # Check if Bruno's speed in the hypothesis is less than or equal to Bruno's speed in the premise
    if bruno_speed_hypothesis <= bruno_speed_premise:
        # The hypothesis is consistent with the premise, so the label is neutral
        print("neutral")
    else:
        # The hypothesis contradicts the premise, so the label is contradiction
        print("contradiction")
else:
    # If Sacha's speed in the hypothesis is less than or equal to Sacha's speed in the premise,
    # then the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    print("neutral")
