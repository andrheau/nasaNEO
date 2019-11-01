import neo_stats
import datetime
import pytz

largest = neo_stats.get_largest_neo()

smallest = neo_stats.get_smallest_neo()

fastest = neo_stats.get_fastest_neo()

asteroid = "{} is the fastest NEO today, racing towards somwhere at a speed of {} kilometers per second.".format(fastest[1], fastest[0])

todays_date = str(datetime.datetime.utcnow().date())

print(todays_date)
