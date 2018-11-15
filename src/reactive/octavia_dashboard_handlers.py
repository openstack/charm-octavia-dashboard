# Copyright 2018 Canonical Ltd
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

import charms.reactive as reactive

import charms_openstack.bus
import charms_openstack.charm as charm

charms_openstack.bus.discover()

# Use the charms.openstack defaults for common states and hooks
charm.use_defaults(
    'charm.installed',
    'config.changed',
    'update-status')


@reactive.when('dashboard.available')
def dashboard_available():
    """Relation to OpenStack Dashboard principal charm complete.
    """
    # config and restart is handled by package install, just update our status
    with charm.provide_charm_instance() as octavia_dashboard_charm:
        octavia_dashboard_charm.assess_status()
