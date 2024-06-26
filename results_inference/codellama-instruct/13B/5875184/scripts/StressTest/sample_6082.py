premise = "If Rahul finds that he is less than 62 th from the right in a line of boys and 4 th from the left, how many boys should be added to the line such that there are 28 boys in the line?"
hypothesis = "If Rahul finds that he is 12 th from the right in a line of boys and 4 th from the left, how many boys should be added to the line such that there are 28 boys in the line?"

# extract the numerical entities from the premise and hypothesis
premise_right_position = int(premise.split(" ")[-2])
premise_left_position = int(premise.split(" ")[-1])
hypothesis_right_position = int(hypothesis.split(" ")[-2])
hypothesis_left_position = int(hypothesis.split(" ")[-1])

# check if the hypothesis value contradicts the premise value
if hypothesis_right_position < premise_right_position:
    label = "contradiction"
elif hypothesis_left_position!= premise_left_position:
    label = "contradiction"
else:
    label = "neutral"

print(label)
