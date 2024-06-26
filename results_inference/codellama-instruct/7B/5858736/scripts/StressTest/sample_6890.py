# Define variables for the number of people and the person who does not want to sit on the middle seat or at either end
num_people = 6
person_not_wanting_to_sit = "Rohit"

# Calculate the number of ways to seat the people on the bench
num_ways_to_seat_people = 6! / (6 - num_people)!

# Check if the hypothesis value contradicts the premise value
if num_ways_to_seat_people!= 7:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise value, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
