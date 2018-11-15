# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function

import charms_openstack.test_utils as test_utils

import charm.openstack.octavia_dashboard as octavia_dashboard


class TestOctaviaDashboardHandlers(test_utils.PatchHelper):

    def test_install(self):
        # we do not care about the internals of the function we are overriding
        # and expanding so mock out the call to super()
        self.patch_object(octavia_dashboard, 'ch_fetch')
        self.patch('builtins.super', 'super')
        c = octavia_dashboard.OctaviaDashboardCharm()
        c.install()
        self.ch_fetch.filter_installed_packages.return_value = []
        self.ch_fetch.filter_installed_packages.assert_called_with(
            c.purge_packages)
        self.ch_fetch.apt_purge.assert_called_with(
            fatal=True,
            packages=c.purge_packages)
        self.super.assert_called()
