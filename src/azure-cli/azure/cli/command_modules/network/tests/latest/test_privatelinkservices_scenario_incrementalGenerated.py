# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_private_link_service
from .example_steps import step_private_link_service2
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network
    # STEP NOT FOUND: /Subnets/put/Create subnet
    # STEP NOT FOUND: /PublicIPAddresses/put/Create public IP address defaults
    # STEP NOT FOUND: /LoadBalancers/put/Create load balancer with Frontend IP in Zone 1
    # STEP NOT FOUND: /PrivateLinkServices/put/Create private link service
    # # # STEP NOT FOUND: /PrivateLinkServices/put/approve or reject private end point connection for a private link service
    step_private_link_service(test, checks=[])
    step_private_link_service2(test, checks=[])
    # STEP NOT FOUND: /PrivateLinkServices/get/Get list of private link service id that can be linked to a private end \
    point with auto approved
    # STEP NOT FOUND: /PrivateLinkServices/get/Get private link service
    # STEP NOT FOUND: /PrivateLinkServices/get/Get list of private link service id that can be linked to a private end \
    point with auto approved
    step_private_link_service2(test, checks=[])
    # STEP NOT FOUND: /PrivateLinkServices/get/List all private list service
    # STEP NOT FOUND: /PrivateLinkServices/post/Check private link service visibility
    # STEP NOT FOUND: /PrivateLinkServices/post/Check private link service visibility
    # STEP NOT FOUND: /PrivateLinkServices/delete/delete private end point connection for a private link service
    # STEP NOT FOUND: /PrivateLinkServices/delete/Delete private link service
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class PrivatelinkservicesScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(PrivatelinkservicesScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myApplicationGateway': 'appgw',
            'myCustomIpPrefix': 'test-customipprefix',
            'myInboundNatRule': self.create_random_name(prefix='natRule1.1'[:5], length=10),
            'myNetworkInterface': 'nic1',
            'myDefaultSecurityRule': 'AllowVnetInBound',
            'myNetworkWatcher': 'nw1',
            'myPublicIpAddress': 'pub1',
            'myVirtualNetwork': 'vnetName',
            'mySubnet': 'subnet1',
            'myVirtualNetworkGatewayConnection': 'vpngw',
            'myVpnSiteLink': 'vpnSiteLink1',
            'myVpnConnection': 'vpnConnection1',
            'myP2sVpnGateway': 'p2svpngateway',
            'myVirtualNetworkGateway': 'vpngateway',
        })

    @ResourceGroupPreparer(name_prefix='clitestnetwork_rg1'[:7], key='rg', parameter_name='rg')
    def test_privatelinkservices_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
