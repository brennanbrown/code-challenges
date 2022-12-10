import datetime

def get_weekday(year, month, day):
  # Create a datetime object with the given year, month, and day
  date = datetime.date(year, month, day)
  
  # Use the `strftime` method to get the name of the day of the week
  # The `%A` format string specifies to print the full name of the day (e.g. "Monday")
  return date.strftime("%A")

# Here's an example of how you can use this function:

# Print the name of the day of the week for December 10, 2022
print(get_weekday(2022, 12, 10))  # Output: "Saturday"

# This function will work correctly for any date within the range of dates that can be represented by the datetime module in Python (approximately the years 1 to 9999).
