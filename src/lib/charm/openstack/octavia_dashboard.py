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

import charms_openstack.adapters
import charms_openstack.charm


class OctaviaDashboardCharm(charms_openstack.charm.OpenStackCharm):
    release = 'rocky'
    name = 'octavia-dashboard'
    packages = ['python3-octavia-dashboard']
    purge_packages = ['python3-neutron-lbaas-dashboard']
    python_version = 3
    adapters_class = charms_openstack.adapters.OpenStackRelationAdapters
    required_relations = ['dashboard']
