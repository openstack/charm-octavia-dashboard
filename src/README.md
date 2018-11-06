# Overview

This subordinate charm provides the Octavia Dashboard plugin for use with the OpenStack Dashboard.

# Usage

Example minimal deploy:

    juju deploy openstack-dashboard --config openstack-origin=bionic:rocky
    juju deploy openstack-dashboard-octavia --config openstack-origin=bionic:rocky
    juju add-relation \
        openstack-dashboard:dashboard-plugin octavia-dashboard:dashboard

# Bugs

Please report bugs on [Launchpad](https://bugs.launchpad.net/charm-octavia-dashboard/+filebug).

For general questions please refer to the OpenStack [Charm Guide](https://docs.openstack.org/charm-guide/latest/).
