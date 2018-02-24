#!/usr/bin/env python

import package

class Obj2:
    pass


package.instance = Obj2()


from check_instance_ref import check_instance_ref

check_instance_ref()