import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to evaluate? Enter the city name, or input 1 for Chicago, 2 for New York, 3 for Washington:\n').lower()
    while city not in ('1','2','3','Chicago','New York','Washington','chicago','new york','washington'):
        print('Sorry! Apparently, this input is invalid. :( \n                 Try Again!')
        city = input('Which city would you like to evaluate? Enter the city name, or input 1 for Chicago, 2 for New York, 3 for Washington:\n').lower()
    if city in ('1','Chicago','chicago'):
        city = 'chicago.csv'
    elif city in ('2','New York','new york'):
        city = 'new_york_city.csv'
    elif city in ('3','Washington','washington'):
        city = 'washington.csv'
    else:
        print("I'm so sorry, a critical error occurred. Please, return to the beginning.")
        sys.exit()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to evaluate? Enter "all" to not filter or the month name, number, or abbreviation:\n').lower()
    while month not in ('all','1','2','3','4','5','6','january','february','march','april','may','june','January','February','March','April','May','June','jan','feb','mar','apr','may','jun'):
        print('Sorry! Apparently, this input is invalid. :( \n                 Try Again!')
        month = input('Which month would you like to evaluate? Enter "all" to not filter or the month name, number, or abbreviation:\n').lower()
    if month == 'all':
        pass
    elif month in ('1','january','January','jan'):
        month = 'january'
    elif month in ('2','february','February','feb'):
        month = 'february'
    elif month in ('3','march','March','mar'):
        month = 'march'
    elif month in ('4','april','April','apr'):
        month = 'april'
    elif month in ('5','may','May','may'):
        month = 'may'
    elif month in ('6','june','June','jun'):
        month = 'june'
    else:
        print("I'm so sorry, a critical error occurred. Please, return to the beginning.")
        sys.exit()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of the week would you like to evaluate? Enter "all" to not filter or the day name or number (Sunday is the first day <=> Sunday = 1):\n').lower()
    while day not in ('all','1','2','3','4','5','6','7','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','sunday','monday','tuesday','wednesday','thursday','friday','saturday'):
        print('Sorry! Apparently, this input is invalid. :( \n                 Try Again!')
        day = input('Which day of the week would you like to evaluate? Enter "all" to not filter or the day name or number (Sunday is the first day <=> Sunday = 1):\n').lower()
    if day == 'all':
        pass
    elif day in ('1','Sunday','sunday'):
        day = 'sunday'
    elif day in ('2','Monday','monday'):
        day = 'monday'
    elif day in ('3','Tuesday','tuesday'):
        day = 'tuesday'
    elif day in ('4','Wednesday','wednesday'):
        day = 'wednesday'
    elif day in ('5','Thursday','thursday'):
        day = 'thursday'
    elif day in ('6','Friday','friday'):
        day = 'friday'
    elif day in ('7','Saturday','saturday'):
        day = 'saturday'
    else:
        print("I'm so sorry, a critical error occurred. Please, return to the beginning.")
        sys.exit()
    print('\n')
    print('-'*40)
    print('\n')
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

# The blanks in this function have been erased. 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(f"The most common month: ",df['month'].mode()[0]) 
    print(f"The most common day of week: ",df['day'].mode()[0])
    print(f"The most common start hour: ",df['hour'].mode()[0])
    print("\nThis took %.2fms." % ((time.time() - start_time)*1000))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip: ',df[df['Start Station']==df['End Station']]['Start Station'].mode()[0])

    print("\nThis took %.2fms." % ((time.time() - start_time)*1000))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Display mean travel time: ',df['Trip Duration'].mean())

    print("\nThis took %.2fms." % ((time.time() - start_time)*1000))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('\n\nCounts of gender: ',df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\n\nEarliest year of birth: ',df['Birth Year'].min())
    print('Most recent year of birth: ',df['Birth Year'].max())
    print('Most common year of birth: ',df['Birth Year'].mode()[0])

    print("\nThis took %.2fms." % ((time.time() - start_time)*1000))
    print('-'*40)

def raw_data(df):
    pd.set_option('display.max_columns', None)
    aux = input(str('Want to see the raw data (the first 5 lines)? Enter yes or no.\n')).lower()
    if aux == 'yes':    
        print(df.head())
    beginning = 5
    end = 10
    aux = input(str('Would you like to see 5 more lines? Enter yes or no.\n')).lower()
    while aux == 'yes':
        print(df.iloc[beginning:end])
        beginning = beginning + 5
        end = end + 10
        aux = input(str('Would you like to see 5 more lines? Enter yes or no.\n')).lower()
        
        
def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.columns)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
