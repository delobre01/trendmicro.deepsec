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

from ansible_collections.trendmicro.deepsec.plugins.action.deepsec_scheduled_tasks import (
    ActionModule,
)


RESPONSE_PAYLOAD = [
    {
        "id": 1,
        "name": "daily_malware_scan",
        "type": "scan-for-malware",
        "enabled": True,
        "recurrence_type": "daily",
        "start_time": 1609459200000,
    },
]

REQUEST_PAYLOAD = [
    {
        "name": "daily_malware_scan",
        "type": "scan-for-malware",
        "enabled": True,
        "recurrence_type": "daily",
        "start_time": 1609459200000,
    },
    {
        "name": "weekly_integrity_scan",
        "type": "scan-for-integrity-changes",
        "enabled": True,
        "recurrence_type": "weekly",
        "start_time": 1609459200000,
    },
]


class TestDeepsecScheduledTasks(unittest.TestCase):
    def setUp(self):
        task = MagicMock(Task)
        task.check_mode = False
        play_context = MagicMock()
        play_context.check_mode = False
        connection = patch(
            "ansible_collections.trendmicro.deepsec.plugins.action.deepsec_scheduled_tasks.Connection",
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
        self._plugin._task.action = "deepsec_scheduled_tasks"
        self._plugin.api_return = "scheduled_tasks"
        self._task_vars = {}

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_scheduled_tasks_merged(self, connection):
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = []
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin._task.args = {
            "state": "merged",
            "config": REQUEST_PAYLOAD,
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_scheduled_tasks_merged_idempotent(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD
        self._plugin._task.args = {
            "state": "merged",
            "config": [
                {
                    "name": "daily_malware_scan",
                    "type": "scan-for-malware",
                    "enabled": True,
                    "recurrence_type": "daily",
                    "start_time": 1609459200000,
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        config_response = {
            "id": 1,
            "name": "daily_malware_scan",
            "type": "scan-for-malware",
            "enabled": True,
            "recurrence_type": "daily",
            "start_time": 1609459200000,
        }

        self.assertEqual(result["scheduled_tasks"]["before"][0]["name"], config_response["name"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_scheduled_tasks_replaced(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD
        self._plugin._task.args = {
            "state": "replaced",
            "config": [
                {
                    "name": "daily_malware_scan",
                    "type": "check-for-security-updates",
                    "enabled": True,
                    "recurrence_type": "hourly",
                    "recurrence_count": 6,
                    "start_time": 1609459200000,
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_scheduled_tasks_replaced_idempotent(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = [
            {
                "id": 1,
                "name": "daily_malware_scan",
                "type": "check-for-security-updates",
                "enabled": True,
                "recurrence_type": "hourly",
                "recurrence_count": 6,
                "start_time": 1609459200000,
            },
        ]
        self._plugin._task.args = {
            "state": "replaced",
            "config": [
                {
                    "name": "daily_malware_scan",
                    "type": "check-for-security-updates",
                    "enabled": True,
                    "recurrence_type": "hourly",
                    "recurrence_count": 6,
                    "start_time": 1609459200000,
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_scheduled_tasks_deleted(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD
        self._plugin._task.args = {
            "state": "deleted",
            "config": [
                {
                    "name": "daily_malware_scan",
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertTrue(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_scheduled_tasks_deleted_idempotent(self, connection):
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = []
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin._task.args = {
            "state": "deleted",
            "config": [
                {
                    "name": "daily_malware_scan",
                },
            ],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])

    @patch("ansible.module_utils.connection.Connection.__rpc__")
    def test_deepsec_scheduled_tasks_gathered(self, connection):
        self._plugin._connection.socket_path = tempfile.NamedTemporaryFile().name
        self._plugin._connection._shell = MagicMock()
        self._plugin.search_for_resource_name = MagicMock()
        self._plugin.search_for_resource_name.return_value = RESPONSE_PAYLOAD
        self._plugin._task.args = {
            "state": "gathered",
            "config": [{"name": "daily_malware_scan"}],
        }
        result = self._plugin.run(task_vars=self._task_vars)
        self.assertFalse(result["changed"])
