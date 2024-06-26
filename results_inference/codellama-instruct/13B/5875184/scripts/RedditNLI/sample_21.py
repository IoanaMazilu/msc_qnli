premise = "Never forget the USA is the best in everything... except for the part where 50% of children and 90% of black children need government assistance to eat."
hypothesis = "The US is quickly becoming a 3rd world country. 50% of all children and 90% of black children need government assistance to eat."

# extract the percentage of children and black children needing government assistance from the premise
premise_percentage = premise.split(" ")[-1]

# extract the percentage of children and black children needing government assistance from the hypothesis
hypothesis_percentage = hypothesis.split(" ")[-1]

# check if the percentage of children and black children needing government assistance in the hypothesis contradicts the premise
if hypothesis_percentage > premise_percentage:
    label = "contradiction"
else:
    label = "neutral"

print(label)
