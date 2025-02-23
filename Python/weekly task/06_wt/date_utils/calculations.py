# hw06
from datetime import datetime, timedelta

def days_between(date, days):
    return (timedelta(days=days)).days - (date).day

def add_days(date, days):
    return (date + timedelta(days=days)).day