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
    for city in CITY_DATA:
        city = input('please choose which city you want \n: chicago, new york city, washington:  ').lower()
        if city not in CITY_DATA:
            print('sorry!!  Please choose a correct  city')
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    for month in months:
        month = input('wich  month do you want to choose \n all, january, february, march, april, may, june  ').lower()
        if month not in months:
            print('sorry!!  Please  choose from the months above  or "aLL "')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    for day in days:
        day = input('please choose a day \n .sunday, monday, tuesday, wednesday, thursday, friday, saturday, all  ').lower()
        if day not in days:
            print('sorry , please Rewrite the correct name of  day or write all')
        else:
            break       
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
  import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    common_start_s = df['Start Station'].mode()[0]
    common_end_s=df['End Station'].mode()[0]
    types_of_user = df['User Type'].value_counts()
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
   # filter by day of week if applicable
    if day != 'all':
      # filter by day of week to create the new dataframe
      df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #df['month'] = df['Start Time'].dt.month
    Frequent_month = df['month'].mode()[0]
    print("The most common month is :\n",Frequent_month)

    # TO DO: display the most common day of week
    #df['day_week'] = df['Start Time'].dt.week
    Frequent_day = df['day_of_week'].mode()[0]
    print("The most common day is :\n",Frequent_day)

    # TO DO: display the most common start hour
     # extract hour from the Start Time column to create an hour column
     # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('the Most Popular Start Hour is:\n',( popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_s = df['Start Station'].mode()[0]
    print("the pouplar start station is \n"+common_start_s)

    # TO DO: display most commonly used end station
    common_end_s=df['End Station'].mode()[0]
    print("the pouplar end station is :\n"+common_end_s)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination_s= (df['Start Station'] + "to" + df['End Station']).mode()[0]
    print("the most frequent combination  is : \n  ",frequent_combination_s)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("the total travel time :\n",total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("the average trip duration is :\n",mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types_of_user = df['User Type'].value_counts()
    print("\nthe type of user at city is : \n",types_of_user)
    
    
    # TO DO: Display counts of gender
    try:
        print('The amount and gender of users in', city, 'are as followed:\n',df['Gender'].value_counts())
    except :
        print('SORRY !the city you select it doesnot have  information of gender \n ')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earl_birth =   df['Birth Year'].min()
        Recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('The Earliest birth  for customer is: {}\n'.format(Earl_birth))
        print('The youngest customers was born in : {}\n'.format(Recent_birth))
        print('Most common birth for our customers is,: {}\n'.format(common_birth))
    except: 
        print("sorry there is no informtion for these city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_row(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next_rows = 0
    while True:
        view_row = input('\nWould you like to view more of trip  data? \n please Enter yes or no.\n')
        if view_row.lower() != 'yes':
            return
        next_rows = next_rows + 8
        print(" Here is the rows you want to Display :\n",df.iloc[next_rows:next_rows+5])
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_row(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
