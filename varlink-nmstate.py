#!/usr/bin/python3 -tt
# Copyright 2019 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# vim: fileencoding=utf8

import os


import libnmstate.netapplier
import libnmstate.netinfo
import varlink

service = varlink.Service(
    vendor='Nmstate',
    product='Nmstate',
    version='0',
    url='http://nmstate.io',
    interface_dir=os.path.dirname(__file__)
)


class ServiceRequestHandler(varlink.RequestHandler):
    service = service


@service.interface('io.nmstate')
class NMState(object):
    def Get(self):
        return {"state": libnmstate.netinfo.show()}

    def Set(self, state):
        libnmstate.netapplier.apply(state)
        return {"state": libnmstate.netinfo.show()}


def run_server(address):
    with varlink.ThreadingServer(address, ServiceRequestHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    run_server("unix:varlink_test")
