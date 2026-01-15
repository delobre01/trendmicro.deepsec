# Copyright (c) 2022 Red Hat
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import tempfile
import unittest

from unittest.mock import MagicMock, patch

from ansible.playbook.task import Task
from ansible.template import Templar

from ansible_collections.trendmicro.deepsec.plugins.action.deepsec_directory_lists import ActionModule


RESPONSE_PAYLOAD = {
    "directory_lists": [
        {
            "id": 1,
            "name": "test_directory_list_1",
            "description": "Directory list 1 for scan exclusion",
            "items": [
                "/tmp/exclude1",
                "/var/log/exclude1",
            ],
        },
    ],
}

REQUEST_PAYLOAD = [
    {
        "name": "test_directory_list_1",
        "description": "Directory list 1 for scan exclusion",
        "items": [
            "/tmp/exclude1",
            "/var/log/exclude1",
        ],
    },
    {
        "name": "test_directory_list_2",
        "description": "Directory list 2 for scan inclusion",
        "items": [
            "/home/include1",
            "/opt/include1",
        ],
    },
]


class TestDeepsecDirectoryLists(unittest.TestCase):
    def setUp(self):
        task = MagicMock(Task)
        # Ansible > 2.13 looks for check_mode in task
        task.check_mode = False
        play_context = MagicMock()
        # Ansible <= 2.13 looks for check_mode in play_context
        play_context.check_mode = False
        connection = patch(
            "ansible_collections.trendmicro.deepsec.plugins.action.deepsec_directory_lists.Connection",
        )
        fake_loader = {}
        templar = Templar(loader=fake_loader)
        self._plugin = ActionModule(
            task=task,
            connection=connection,
            play_context=play_context,
            loader=fake_loader,
            templar=templar,
            shared_loader_obj=None,
        )
        self._plugin._task.action = "directory_lists"
        self._plugin.api_return = "directory_lists"
        self._task_vars = {}

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_directory_lists_merged(self, connection):
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = {}
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin._task.args = {
            "state": "merged",
            "config": REQUEST_PAYLOAD,
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_directory_lists_merged_idempotent(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD

        self._plugin._task.args = {
            "state": "merged",
            "config": [
                {
                    "name": "test_directory_list_1",
                    "description": "Directory list 1 for scan exclusion",
                    "items": [
                        "/tmp/exclude1",
                        "/var/log/exclude1",
                    ],
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_directory_lists_replaced(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD

        self._plugin._task.args = {
            "state": "replaced",
            "config": [
                {
                    "name": "test_directory_list_1",
                    "description": "REPLACED Directory list 1",
                    "items": [
                        "/tmp/replaced1",
                    ],
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_directory_lists_gathered(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD

        self._plugin._task.args = {
            "state": "gathered",
            "config": [
                {
                    "name": "test_directory_list_1",
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
        self.assertIn("gathered", result)

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_directory_lists_deleted(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD

        self._plugin._task.args = {
            "state": "deleted",
            "config": [
                {
                    "name": "test_directory_list_1",
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_directory_lists_overridden(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = {}
        
        mock_conn_request = MagicMock()
        mock_conn_request.get.return_value = (200, RESPONSE_PAYLOAD)
        mock_conn_request.delete.return_value = (200, {})
        mock_conn_request.post.return_value = (200, RESPONSE_PAYLOAD["directory_lists"][0])
        
        with patch("ansible_collections.trendmicro.deepsec.plugins.action.deepsec_directory_lists.DeepSecurityRequest", return_value=mock_conn_request):
            self._plugin._task.args = {
                "state": "overridden",
                "config": [
                    {
                        "name": "test_directory_list_override",
                        "description": "Override directory list",
                        "items": [
                            "/override/path1",
                        ],
                    },
                ],
            }
            result = self._plugin.run(task_vars=self._task_vars)
            self.assertTrue(result["changed"])
