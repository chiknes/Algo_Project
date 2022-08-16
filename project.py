def buildGraph(cab_dataset):


# select pickup_location, dropoff_location and distance from the dataset
# create adjacency matrix with pickup and dropoff as vertices and distance as edges
# return adjacency_matrix


def buildPassengerData(startingLocation, endingLocation, timeframes):


# startingLocation, endingLocation will be fixed values that is passed to the method depending on the testcase that we are working on
# timeframes will be the list of timeframes to add timestamp for booking (eg: 7:00-8:00, 9:00-10:00 etc)
# Add passenger data to cover all test cases - use dummy data with different timestamps to cover all scenarios
# Dataframe should contain - passenger_id, booking_timestamp, dropoffLocation, denials
# Return dataframe - this will be used to add passengers to the priority queue for bookings


def allocatePassengerSeats(adjacency_matrix, filtered_pass_data, thresholds):
# Passengers with higher denails and eralier booking time should be at the top

# Now select top 8 records from the data and start iterations:
# Iter 1: min_cost route is found, now select other 10 people from the list to perform some more permuations/combinations
# If another min_cost route found then include that path as a BUS route and select those 8 passengers for BUS 1

# Remove allocated passangers from waiting queue and increas the denial count against passenegers evluated in Iter 1
# Iter 2: Now, select another 8 passengers from the remaining list and perform MST. Again select 10 more passenegers and look for possible MST
# If MST is found for any passenger(s) then include it as a route for BUS 2 and allocate seats to those 8 passengers

# Repeat above till algorithm finishes with BUS 5 or all records are processed.

# retun dictionary of {BUS:{passenger_ids, route, cost}}, updated_passenger_data_file(basically with updated denial ccounts)
