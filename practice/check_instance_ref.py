#!/usr/bin/env python

from package import instance


def check_instance_ref():
    type = instance.__class__.__name__

    print 'type: {var}'.format(var=type)
