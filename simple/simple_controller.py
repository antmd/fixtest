""" Simple controller used for testing.

    Copyright (c) 2014 Kenn Takara
    See LICENSE for details

"""

import logging

from fixtest.base.controller import TestCaseController
from fixtest.base.utils import log_text


class SimpleController(TestCaseController):
    """ The base class for FIX-based TestCaseControllers.
    """
    def __init__(self, **kwargs):
        super(SimpleController, self).__init__(**kwargs)

        self._servers = dict()
        self._clients = dict()

        server = {
            'name': 'server-9940',
            'port': 9940,
            'factory': None,
        }
        self._servers[server['name']] = server

        config = kwargs['config']

        self.node_config = config.get_role('test-server')
        self.node_config.update({'name': 'server-9940'})

        self.link_config = config.get_link('client', 'test-server')
        self.link_config.update({
            'sender_compid': self.link_config['test-server'],
            'target_compid': self.link_config['client'],
            })

        self._logger = logging.Logger(__name__)


    def clients(self):
        """ The clients that need to be started """
        return self._clients

    def servers(self):
        """ The servers that need to be started """
        return self._servers

    def setup(self):
        pass

    def teardown(self):
        pass

    def run(self):
        pass
