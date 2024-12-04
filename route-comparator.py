def parse_routes_from_file(file_path):
    """Parse a route table from a file into a set of route entries."""
    routes = set()
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into parts
            parts = line.split()
            # Check if the line has enough parts to process
            if len(parts) > 1:
                # Extract the network portion of the route
                route = parts[1]
                routes.add(route)
    return routes

def find_missing_routes(file1, file2):
    """Find routes that are in file2 but not in file1."""
    routes1 = parse_routes_from_file(file1)
    routes2 = parse_routes_from_file(file2)
    missing_routes = routes2 - routes1
    return missing_routes

# Prompt user for file names
file1 = input("Enter the file name for the 1st route table: ")
file2 = input("Enter the file name for the 2nd route table: ")

# Find missing routes
missing_routes = find_missing_routes(file1, file2)

# Print missing routes
if missing_routes:
    print("Routes in the 2nd table missing from the 1st table:")
    for route in missing_routes:
        print(route)
else:
    print("No missing routes found.")