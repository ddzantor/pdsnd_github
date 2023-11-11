import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# Function to calculate the mean travel time
def mean_travel_time(travel_times):
    """
    Calculate the mean travel time from a list of travel times.

    Args:
        travel_times (list): A list of integers representing travel times in seconds.

    Returns:
        float: The mean travel time in seconds.
    """
    total_travel_time = sum(travel_times)
    mean_time = total_travel_time / len(travel_times)
    return mean_time

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    # City input validation
    while True:
        try:
            city = input('Enter city (Chicago, New York City, Washington): ').lower()
            if city in CITY_DATA:
                break
            else:
                raise ValueError('Invalid input. Please enter a valid city.')
        except ValueError as e:
            print(e)

    # Month input validation
    while True:
        try:
            month = input('Enter month (all, January, February, March, April, May, June): ').lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                raise ValueError('Invalid input. Please enter a valid month.')
        except ValueError as e:
            print(e)

    # Day input validation
    while True:
        try:
            day = input('Enter day of the week (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ').lower()
            if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                raise ValueError('Invalid input. Please enter a valid day of the week.')
        except ValueError as e:
            print(e)

    print('-'*40)
    return city, month, day

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    time_units = {
        'Month': 'month',
        'Day of Week': 'day of week',
        'Hour': 'start hour'
    }

    for unit, label in time_units.items():
        df[unit] = df['Start Time'].dt.__getattribute__(label)

    for unit in time_units:
        common_unit = df[unit].mode()[0]
        print(f'Most Common {unit}: {common_unit}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))
    
    most_common_combination = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('The most popular combination is: {}'.format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()

    print('Total travel time: {} seconds'.format(total_travel_time))
    print('Mean travel time: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Gender distribution
    if 'Gender' in df:
        print('Gender Distribution:\n', df['Gender'].value_counts())
    else:
        print('Gender data not available for this city.')

    # Birth year information
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])

        print('Earliest Birth Year:', earliest_birth_year)
        print('Most Recent Birth Year:', most_recent_birth_year)
        print('Most Common Birth Year:', most_common_birth_year)
    else:
        print('Birth Year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    start_index = 0
    while True:
        display_raw = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').lower()
        if display_raw != 'yes':
            break
        print(df.iloc[start_index:start_index + 5])
        start_index += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df is not None:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break

if __name__ == "__main__":
    main()
