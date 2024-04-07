# Premise: If Rahul finds that he is 12 th from the right in a line of boys and 4 th from the left, how many boys should be added to the line such that there are 28 boys in the line?
# Hypothesis: If Rahul finds that he is less than 62 th from the right in a line of boys and 4 th from the left, how many boys should be added to the line such that there are 28 boys in the line?
# Golden Label: entailment

position_right_premise = 12
position_right_hypothesis = 62
position_left = 4
boys_in_line_premise = 28
boys_in_line_hypothesis = 28

# the hypothesis talks about Rahul's position in a line and the total number of boys, same as the premise
if position_right_hypothesis < position_right_premise:
    # check if the hypothesis value contradicts the premise value of 'position_right_premise'
    label = "contradiction"
elif boys_in_line_hypothesis != boys_in_line_premise:
    # check if the total number of boys in the hypothesis contradicts the total number of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

