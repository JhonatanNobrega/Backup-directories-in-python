from datetime import datetime, timedelta

def subtractDaysFromCurrentDate(days):
  currentDate = datetime.now()
  result = currentDate - timedelta(days)
  return result.strftime('%Y-%m-%d')
