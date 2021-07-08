from datetime import datetime
string = '2021-12-1'
print(type(datetime.strftime(datetime.strptime(string, '%Y-%m-%d'), "%Y-%m-%d")))
