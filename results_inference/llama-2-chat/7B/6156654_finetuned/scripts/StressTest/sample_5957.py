england_premise = 26
england_hypothesis = 86
france_premise = 26
france_hypothesis = 26
italy_premise = 32
italy_hypothesis = 32

# the hypothesis refers to the number of members of a certain club who traveled to different countries
# as per the premise

# compute the total number of members who traveled to each country in the hypothesis
total_england_hypothesis = england_hypothesis + england_premise
total_france_hypothesis = france_hypothesis + france_premise
total_italy_hypothesis = italy_hypothesis + italy_premise

# check if the number of members who traveled to each country in the hypothesis contradicts the number in the premise
if total_england_hypothesis!= england_premise:
    label = "contradiction"
elif total_france_hypothesis!= france_premise:
    label = "contradiction"
elif total_italy_hypothesis!= italy_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
