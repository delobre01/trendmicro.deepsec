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

from ansible_collections.trendmicro.deepsec.plugins.action.deepsec_policies import (
    ActionModule,
)


RESPONSE_PAYLOAD = {
    "policies": [
        {
            "ID": 10,
            "name": "production_policy",
            "description": "Production server security policy",
            "autoRequiresUpdate": "on",
            "parentID": 1,
            "antiMalware": {
                "state": "on",
                "realTimeScanConfigurationID": 1,
            },
            "firewall": {
                "state": "on",
                "ruleIDs": [1, 2, 3],
            },
        },
    ],
}

REQUEST_PAYLOAD = [
    {
        "name": "production_policy",
        "description": "Production server security policy",
        "auto_requires_update": "on",
        "parent_id": 1,
        "anti_malware": {
            "state": "on",
            "real_time_scan_configuration_id": 1,
        },
        "firewall": {
            "state": "on",
            "rule_ids": [1, 2, 3],
        },
    },
    {
        "name": "web_server_policy",
        "description": "Web server policy",
        "auto_requires_update": "on",
        "firewall": {
            "state": "on",
        },
        "intrusion_prevention": {
            "state": "on",
        },
    },
]


class TestDeepsecPolicies(unittest.TestCase):
    def setUp(self):
        task = MagicMock(Task)
        # Ansible set_options method expects a dictionary, so we pass an empty dict
        self._connection = MagicMock()
        self._connection.socket_path = tempfile.NamedTemporaryFile().name
        play_context = MagicMock()
        play_context.check_mode = False
        fake_loader = MagicMock()
        fake_loader.get_basedir.return_value = "/tmp"
        self._task = MagicMock(Task)
        self._task.action = "deepsec_policies"
        self._task.async_val = False
        self._task._role = None
        self._task.args = {}
        templar = Templar(loader=fake_loader)
        self._action_module = ActionModule(
            task=self._task,
            connection=self._connection,
            play_context=play_context,
            loader=fake_loader,
            templar=templar,
            shared_loader_obj=None,
        )

    def test_deepsec_policies_merged(self):
        """Test merged state"""
        self._task.args = {
            "state": "merged",
            "config": REQUEST_PAYLOAD,
        }
        with patch.object(
            self._action_module,
            "_check_argspec",
        ) as mock_check_argspec:
            with patch.object(
                self._action_module,
                "configure_module_api",
            ) as mock_configure:
                mock_configure.return_value = (
                    {"before": [], "after": RESPONSE_PAYLOAD["policies"]},
                    True,
                )
                result = self._action_module.run(task_vars={})
                self.assertTrue(result["changed"])
                self.assertIn("policies", result)

    def test_deepsec_policies_gathered(self):
        """Test gathered state"""
        self._task.args = {
            "state": "gathered",
            "config": [{"name": "production_policy"}],
        }
        with patch.object(
            self._action_module,
            "_check_argspec",
        ) as mock_check_argspec:
            with patch.object(
                self._action_module,
                "search_for_resource_name",
            ) as mock_search:
                mock_search.return_value = RESPONSE_PAYLOAD["policies"]
                result = self._action_module.run(task_vars={})
                self.assertFalse(result["changed"])
                self.assertIn("gathered", result)

    def test_deepsec_policies_deleted(self):
        """Test deleted state"""
        self._task.args = {
            "state": "deleted",
            "config": [{"name": "production_policy"}],
        }
        with patch.object(
            self._action_module,
            "_check_argspec",
        ) as mock_check_argspec:
            with patch.object(
                self._action_module,
                "delete_module_api_config",
            ) as mock_delete:
                mock_delete.return_value = (
                    {"before": RESPONSE_PAYLOAD["policies"], "after": []},
                    True,
                )
                result = self._action_module.run(task_vars={})
                self.assertTrue(result["changed"])
                self.assertIn("policies", result)

    def test_deepsec_policies_replaced(self):
        """Test replaced state"""
        self._task.args = {
            "state": "replaced",
            "config": REQUEST_PAYLOAD,
        }
        with patch.object(
            self._action_module,
            "_check_argspec",
        ) as mock_check_argspec:
            with patch.object(
                self._action_module,
                "configure_module_api",
            ) as mock_configure:
                mock_configure.return_value = (
                    {
                        "before": RESPONSE_PAYLOAD["policies"],
                        "after": RESPONSE_PAYLOAD["policies"],
                    },
                    True,
                )
                result = self._action_module.run(task_vars={})
                self.assertTrue(result["changed"])
                self.assertIn("policies", result)


if __name__ == "__main__":
    unittest.main()
