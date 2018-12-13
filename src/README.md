# Overview

This subordinate charm provides the Octavia Dashboard plugin for use with the OpenStack Dashboard.

# Usage

Example minimal deploy:

    juju deploy openstack-dashboard --config openstack-origin=cloud:bionic-rocky
    juju deploy octavia-dashboard
    juju add-relation \
        openstack-dashboard:dashboard-plugin octavia-dashboard:dashboard

There is a [section](https://docs.openstack.org/project-deploy-guide/charm-deployment-guide/latest/app-octavia.html) about Octavia in the [Deployment Guide](https://docs.openstack.org/project-deploy-guide/charm-deployment-guide/latest/).

A [bundle overlay](https://github.com/openstack-charmers/openstack-bundles/blob/master/stable/overlays/loadbalancer-octavia.yaml) for use in conjunction with the [OpenStack Base bundle](https://jujucharms.com/openstack-base/) is also available.

# Bugs

Please report bugs on [Launchpad](https://bugs.launchpad.net/charm-octavia-dashboard/+filebug).

For general questions please refer to the OpenStack [Charm Guide](https://docs.openstack.org/charm-guide/latest/).
