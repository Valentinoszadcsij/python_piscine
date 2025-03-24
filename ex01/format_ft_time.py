# here we learn importing packages/modules, extracting time/date data and printing with f-strings	
import datetime as dt
import time as tm

x = dt.datetime.now()
epoch = tm.time()
print(f"Seconds since January 1, 1970: {epoch} or {epoch:.2e} in scientific notation")
print(f"{x.strftime('%b')} {x.day} {x.year}")