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

import charmhelpers.core as ch_core

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
    dashboard = reactive.endpoint_from_flag('dashboard.available')
    ch_core.hookenv.log('DEBUG: dashboard_available "{}" "{}" "{}"'
                        .format(dashboard.release, dashboard.bin_path,
                                dashboard.openstack_dir))
    dashboard.publish_plugin_info({'setting-one-key': 'value-one'}, 'priority')
