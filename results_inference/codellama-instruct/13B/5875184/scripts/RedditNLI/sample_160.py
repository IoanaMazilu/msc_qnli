premise = "GDP Report Shows US Economy Off to Slow Start in 2017."
hypothesis = "U.S. economy off to slow start in 2017 under Trump."

# extract the year from the premise and hypothesis
year_premise = premise.split(" ")[-1]
year_hypothesis = hypothesis.split(" ")[-1]

# check if the year in the hypothesis contradicts the year in the premise
if year_premise!= year_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
