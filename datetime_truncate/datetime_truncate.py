from datetime import timedelta

__all__ = [
    'truncate',
    'first_day_of_week',
    'first_day_of_quarter',
    'first_day_of_half_year',
]

PERIODS = {
    'second': dict(microsecond=0),
    'minute': dict(microsecond=0, second=0),
    'hour': dict(microsecond=0, second=0, minute=0),
    'day': dict(microsecond=0, second=0, minute=0, hour=0,),
    'month': dict(microsecond=0, second=0, minute=0, hour=0, day=1),
    'year': dict(microsecond=0, second=0, minute=0, hour=0, day=1, month=1),
}
ODD_PERIODS = ['week', 'quarter', 'half_year']


def first_day_of_week(dt):
    '''
    Truncates a date to the first day of an ISO 8601 week, i.e. monday.

    :params dt: an initialized datetime object
    :return: `dt` with the original day set to monday
    :rtype: :py:mod:`datetime` datetime object
    '''
    day = dt.isoweekday()
    if day == 1:
        return dt
    elif day > 1:
        return dt - timedelta(days=day - 1)


def first_day_of_quarter(dt):
    '''
    Truncates the datetime to the first day of the quarter for this date.

    :params dt: an initialized datetime object
    :return: `dt` with the month set to the first month of this quarter
    :rtype: :py:mod:`datetime` datetime object
    '''
    month = dt.month
    if month >= 1 and month <= 3:
        return dt.replace(month=1)
    elif month >= 4 and month <= 6:
        return dt.replace(month=4)
    elif month >= 7 and month <= 9:
        return dt.replace(month=7)
    elif month >= 10 and month <= 12:
        return dt.replace(month=10)


def first_day_of_half_year(dt):
    '''
    Truncates the datetime to the first day of the half year for this date.

    :params dt: an initialized datetime object
    :return: `dt` with the month set to the first month of this half year
    :rtype: :py:mod:`datetime` datetime object
    '''
    month = dt.month

    if month >= 1 and month <= 6:
        return dt.replace(month=1)
    elif month >= 7 and month <= 12:
        return dt.replace(month=7)


def truncate(dt, truncate_to='day'):
    '''
    Truncates a datetime to have the values with higher precision than
    the one set as `truncate_to` as zero (or one for day and month).

    Possible values for `truncate_to`:

    * second
    * minute
    * hour
    * day
    * week (iso week i.e. to monday)
    * month
    * quarter
    * half_year
    * year

    Examples::

       > truncate(datetime(2012, 12, 12, 12), 'day')
       datetime(2012, 12, 12)
       > truncate(datetime(2012, 12, 14, 12, 15), 'quarter')
       datetime(2012, 10, 1)
       > truncate(datetime(2012, 3, 1), 'week')
       datetime(2012, 2, 27)

    :params dt: an initialized datetime object
    :params truncate_to: The highest precision to keep its original data.
    :return: datetime with `truncated_to` as the highest level of precision
    :rtype: :py:mod:`datetime` datetime object
    '''
    if truncate_to in PERIODS:
        return dt.replace(**PERIODS[truncate_to])
    elif truncate_to in ODD_PERIODS:
        if truncate_to == 'week':
            return truncate(first_day_of_week(dt), 'day')
        elif truncate_to == 'quarter':
            return truncate(first_day_of_quarter(dt), 'month')
        elif truncate_to == 'half_year':
            return truncate(first_day_of_half_year(dt), 'month')
    else:
        raise ValueError('truncate_to not valid. Valid periods: {}'.format(
            ', '.join(PERIODS.keys() + ODD_PERIODS)
        ))
