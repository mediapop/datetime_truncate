# datetime_truncate

This module truncates a datetime object to the level of precision that
you specify, making everything higher than that zero (or one for day
and month).

It is based on PostgreSQL's [`DATE_TRUNC`](http://www.postgresql.org/docs/9.1/static/functions-datetime.html#FUNCTIONS-DATETIME-TRUNC).

## Usage:

    > from datetime_util import truncate
    > truncate(datetime(2012, 2, 4, 12, 24, 50, 234), 'second')
    datetime(2012, 2, 4, 12, 24, 50)
    > truncate(datetime(2012, 2, 4, 12, 24, 50), 'minute')
    datetime(2012, 2, 4, 12, 24)
    > truncate(datetime(2012, 2, 4, 12, 24), 'hour')
    datetime(2012, 2, 4, 12)
    > truncate(datetime(2012, 2, 4, 12, 24), 'day')
    datetime(2012, 2, 4)
    > truncate(datetime(2012, 2, 4, 12, 24), 'week')
    datetime(2012, 1, 30)
    > truncate(datetime(2012, 2, 4, 12, 24), 'month')
    datetime(2012, 2, 1)
    > truncate(datetime(2012, 2, 4, 12, 24), 'quarter')
    datetime(2012, 1, 1)
    > truncate(datetime(2012, 8, 18, 12, 25), 'half_year')
    datetime(2012, 7, 1)
    > truncate(datetime(2012, 8, 18, 12, 25), 'year')
    datetime(2012, 1, 1)
