distance_east_premise = 156
distance_west_premise = 164
depth_hypothesis = 35

# the hypothesis mentions the depth of the earthquake, which is not referenced in the premise
# the premise mentions the distance of the earthquake from Bitung and Tobelo, which is not referenced in the hypothesis
# there is no numerical information in the premise that can be used to infer the depth of the earthquake from the distances given
label = "neutral"

print(label)
