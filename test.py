#!/bin/python

import unittest

def PomFile(update=False):
    from xml.etree import ElementTree as et
    ns = "http//maven.apache.org/POM/4.0.0"
    et.register_namespace('',ns)
    tree = et.ElementTree()
    tree.parse('pom.xml')
    pom = tree.getroot().find("{%s}version"% ns)
    if update:
	pom.text = update
	tree.write('pom.xml')
    else:
	return pom.xml

print (PomFile())

if __name__ == '__main__':
    unittest.main()
