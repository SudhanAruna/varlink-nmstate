#!/usr/bin/python3 -tt
# Copyright 2019 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# vim: fileencoding=utf8

import json
import sys

import varlink

if __name__ == "__main__":
    command = sys.argv[1]
    if command == "set":
        state = json.loads(open(sys.argv[2]))

    varlink_nmstate_cmd = ["python3", "varlink-nmstate.py"]
    with varlink.Client.new_with_activate(varlink_nmstate_cmd) as client, \
            client.open('io.nmstate') as connection:
        if command == "get":
            print(connection.Get()["state"])
        elif command == "set":
            print(connection.Set(state=state)["state"])
