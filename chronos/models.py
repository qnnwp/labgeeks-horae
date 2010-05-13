from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    """ The location of the punchclock, as well as the location staff are signing in for. This lets us use multiple computers on site as punchclocks.
    """
    name = models.CharField(max_length=256)
    active_users = models.ManyToManyField(User, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Punchclock(models.Model):
    """ The computer we'll check ip address against to make sure staff are allowed to sign in from here.
    """
    name = models.CharField(max_length=256)
    location = models.ForeignKey(Location)
    ip_address = models.IPAddressField()

    def __unicode__(self):
        return self.name

class Shift(models.Model):
    """ The shift the user is signing into or out of. A historical record of a work session.
    """
    person = models.ForeignKey(User)
    intime = models.DateTimeField()
    outtime = models.DateTimeField(blank=True, null=True)
    punchclock = models.ForeignKey(Punchclock)
    shiftnote = models.TextField(blank=True)

    def __unicode__(self):
        return "%s@[%s]-[%s]" % (self.person, self.intime, self.outtime)
