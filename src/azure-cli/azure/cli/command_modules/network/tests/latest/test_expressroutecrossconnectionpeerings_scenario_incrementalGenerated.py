# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_express_route_cross_connection_peering_create
from .example_steps import step_express_route_cross_connection_peering_show
from .example_steps import step_express_route_cross_connection_peering_delete
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
    step_express_route_cross_connection_peering_create(test, checks=[])
    step_express_route_cross_connection_peering_show(test, checks=[])
    # STEP NOT FOUND: /ExpressRouteCrossConnectionPeerings/get/ExpressRouteCrossConnectionBgpPeeringList
    step_express_route_cross_connection_peering_delete(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class ExpressroutecrossconnectionpeeringsScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(ExpressroutecrossconnectionpeeringsScenarioTest, self).__init__(*args, **kwargs)
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
    def test_expressroutecrossconnectionpeerings_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
