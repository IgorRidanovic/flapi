#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Filmlight FLAPI connection loader for a Baselight host at a specific IP address.
Returns a tuple where [0] element is the connection object or False if connection is unavailable,
and [1] is the status message. You must allow traffic on ports 1984 and 5432.

Copyright (c) 2020 Igor Riđanović, Igor [at] hdhead.com, www.metafide.com
'''

import flapi

def getflapi(ip='localhost'):

	c = flapi.Connection(ip)

	try:
		c.connect()
		msg = 'FLAPI is connected.'

		# Test PostgreSQL response because port 5432 may be closed.
		testResponse = c.JobManager.get_jobs(ip)
		if '5432' in testResponse:
			msg = msg + ' However, port 5432 is closed.'
			return False, msg

		return c, msg

	except flapi.FLAPIException as ex:
		msg = 'Not connected to FLAPI: \n%s.' %ex
		return False, msg

if __name__ == '__main__':

	conn, msg = getflapi()

	# Remote host
#	ip4 = Some IP Address
#	conn, msg = getflapi(ip4)
	
	print msg

	if conn != False:
		print 'Ready to do stuff.'

	else:
		print 'Sorry. Not ready.'
