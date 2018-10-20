import datetime

class Base(object):
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7)

class Dev(Base):
    DEBUG = True