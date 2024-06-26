sacha_speed_premise = 7
bruno_speed_premise = 5
sacha_speed_hypothesis = float(input("Enter Sacha's speed (less than 7): "))
bruno_speed_hypothesis = float(input("Enter Bruno's speed (5): "))

# check if Sacha's speed contradicts the premise
if sacha_speed_hypothesis > sacha_speed_premise:
    label = "contradiction"
elif bruno_speed_hypothesis!= bruno_speed_premise:
    # check if Bruno's speed contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
