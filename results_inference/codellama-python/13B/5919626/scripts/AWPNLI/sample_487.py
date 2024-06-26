orange_balloons_premise = 9.0
blue_balloons_premise = 4.0
orange_balloons_found_premise = 2.0
orange_balloons_hypothesis = 13.0

# the hypothesis talks about the number of orange balloons, which are also referenced in the premise
# find the total number of balloons from the premise 
total_balloons_premise = orange_balloons_premise + blue_balloons_premise
if orange_balloons_hypothesis!= total_balloons_premise:
    # check if the total balloons from the hypothesis contradict the estimate of more than 'orange_balloons_premise'
    label = "contradiction"
elif orange_balloons_hypothesis!= orange_balloons_premise + orange_balloons_found_premise:
    # check if the number of orange balloons from the hypothesis contradicts the number of orange balloons in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
