graduated_premise = "The Citadel"
officer_premise = "U.S. Air Force"
head_hypothesis = "South Carolina Hospitality Association"

# define variables with representative names for the numerical entities in both inputs
graduated = "Sponseller graduated from The Citadel"
officer = "Sponseller is a former officer in the U.S. Air Force"
head = "Tom Sponseller, 61, is head of the South Carolina Hospitality Association"

# extract all quantities as valid numbers (integers or floats)
graduated_value = None
officer_value = None
head_value = None

# check if the hypothesis mentions any numerical information
if "61" in head:
    head_value = 61

# compare the numerical information in the premise and hypothesis
if graduated_value!= officer_value:
    # check if the graduation information contradicts the officer information
    label = "contradiction"
elif graduated_value == officer_value:
    # check if the graduation and officer information are the same
    label = "neutral"
elif head_value!= graduated_value:
    # check if the head information contradicts the graduation information
    label = "contradiction"
elif head_value == graduated_value:
    # check if the head and graduation information are the same
    label = "entailment"

# print the label
print(label)
