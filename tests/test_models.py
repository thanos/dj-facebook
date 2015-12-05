#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-facebook
------------

Tests for `dj-facebook` models module.
"""
import pprint

from django.test import TestCase

from djfacebook import models


class TestDjfacebook(TestCase):

    def setUp(self):
        pass

    def test_something(self):
        import fb, os
        TOKEN = os.environ['TOKEN']
        facebook = fb.graph.api(TOKEN)
        p = facebook.get_object(cat = "single", id='MykonosBiennale/posts', fields = [ ])
        pprint.pprint(p['data'][0])
        print p['data'][0]['description']


    def tearDown(self):
        pass
