# 99.010 Dates and Times

## The problem with date notation

In the US we have traditionally denoted dates as Month/Day/Year.  So Christmas in 2022 is 12/25/2022.

But in much of Europe dates are traditionally written Day/Month/Year.  So Christmas in 2022 is 25/12/2022.

Inspection shows whether the date of Christmas is written in.  There are no month with 25 days in them, so it is easy to tell that 25/12/2022 was written by an American or a European.

### Ambiguity

But what about 4/2/2022?   Does that mean April 2, 2022 or does it mean February 4, 2022?  This became a big problem as the world became more international, especially with the the introduction of the Internet.  

### Sorting

Another problem with both M/D/Y and D/M/Y is sorting.  It is common to sort by date.  But for a computer to sort the traditional notation the date must be taken apart and sorted in parts.

## IS0 8601

Reference: [https://en.wikipedia.org/wiki/ISO_8601](https://en.wikipedia.org/wiki/ISO_8601)

"ISO" is The International Standards Organization.  As the name suggests, the ISO sets international standards.

The ISO format for dates uses Y-M-D format.  It also specifies that the month and day must be written as two digits, even if a leading zero is needed.  ISO dates would look like 2022-12-25 and 2022-04-02.  

The ISO format removes ambiguity, It doesn't favor either the American or European tradition.  And, from an IT perspective, it makes the date sortable as if it is a string.

### ISO Times

ISO 8601 also covers times.  It uses the concept of descending order.  So hours are listed as hours-minutes-seconds.  This preserves sortability, although there are some problems with 24-hour vs AM/PM notation.  We are not going to be overly concerned with dates in this course.

## Time Zones

### UCT

Time zones are established based on 0 longitude.  0 longitude passes through the Royal Observatory in Greenwich, England.

### Other notations:

* UTC -- Universal Time Coordinated or Universal Coordinated Time
* GMT -- Greenich Mean Time
* Z -- Zulu - Often used in military

UTC does not observe Daylight Savings Time

## Time Zones

Timezones are measured based on UTC.  Central Standard Time used in St. Joseph Missouri is 6 hours behind UTC.  So CST is referred to as UTC-6.   When Daylight Savings Time is in effect Central time is UTC-5.

Central time in the US is often referred to as America/Chicago

## Time Stamps

Timestamps in Unix and many computer operations use timestamps.  Timestamps are measured in terms of the number of seconds since midnight on January 1, 1970.  So a timestamp would look like 1638447563.

## Dates in Python

Python uses the datetime package to manipulate dates.

```python
import datetime

t = datetime.datetime.now()
print("\nThe current time:")
print(t)

ts = 1638447563

t = datetime.datetime.fromtimestamp(ts)
print(f"\nThe timestamp {ts} represents {ts} seconds since 1970-01-01Z00:00:00")
print(t)

t=datetime.datetime.fromtimestamp(0)
print(f"\nThe date corresponding to {ts}")
print(t)
```

The above code produces the following output as I produce this document.

```text
The current time:
2021-12-02 06:30:55.147485

The timestamp 1638447563 represents 1638447563 seconds since 1970-01-01Z00:00:00
2021-12-02 06:19:23

The date corresponding to 1638447563
1969-12-31 18:00:00
```

For more information see the following:

* The basics: [https://www.w3schools.com/python/python_datetime.asp](https://www.w3schools.com/python/python_datetime.asp)
* More complete documentation: [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)