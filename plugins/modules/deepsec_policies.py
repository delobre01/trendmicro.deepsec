#!/usr/bin/python
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: deepsec_policies
short_description: Manages Policy resource module
description: Policy details for TrendMicro Deep Security.
version_added: 1.3.0
options:
  config:
    description: A dictionary of Policy options
    type: list
    elements: dict
    suboptions:
      id:
        description: ID of the policy. Searchable as ID.
        type: int
      name:
        description: Name of the policy. Searchable as String.
        type: str
      description:
        description: Description of the policy. Searchable as String.
        type: str
      parent_id:
        description: Parent policy ID for inheritance. Searchable as Numeric.
        type: int
      auto_requires_update:
        description: Auto-update behavior. Searchable as Choice.
        type: str
        choices:
          - on
          - off
      recommendation_scan_mode:
        description: Recommendation scan mode. Searchable as Choice.
        type: str
        choices:
          - off
          - ongoing
      anti_malware:
        description: Anti-malware policy extension settings
        type: dict
        suboptions:
          state:
            description: State of the anti-malware module
            type: str
            choices:
              - on
              - off
              - inherited
          real_time_scan_configuration_id:
            description: Real-time scan configuration ID
            type: int
          scheduled_scan_configuration_id:
            description: Scheduled scan configuration ID
            type: int
          manual_scan_configuration_id:
            description: Manual scan configuration ID
            type: int
      firewall:
        description: Firewall policy extension settings
        type: dict
        suboptions:
          state:
            description: State of the firewall module
            type: str
            choices:
              - on
              - off
              - inherited
          rule_ids:
            description: List of firewall rule IDs
            type: list
            elements: int
      intrusion_prevention:
        description: Intrusion prevention policy extension settings
        type: dict
        suboptions:
          state:
            description: State of the intrusion prevention module
            type: str
            choices:
              - on
              - off
              - inherited
          rule_ids:
            description: List of intrusion prevention rule IDs
            type: list
            elements: int
      integrity_monitoring:
        description: Integrity monitoring policy extension settings
        type: dict
        suboptions:
          state:
            description: State of the integrity monitoring module
            type: str
            choices:
              - on
              - off
              - inherited
          rule_ids:
            description: List of integrity monitoring rule IDs
            type: list
            elements: int
      log_inspection:
        description: Log inspection policy extension settings
        type: dict
        suboptions:
          state:
            description: State of the log inspection module
            type: str
            choices:
              - on
              - off
              - inherited
          rule_ids:
            description: List of log inspection rule IDs
            type: list
            elements: int
      web_reputation:
        description: Web reputation policy extension settings
        type: dict
        suboptions:
          state:
            description: State of the web reputation module
            type: str
            choices:
              - on
              - off
              - inherited
      application_control:
        description: Application control policy extension settings
        type: dict
        suboptions:
          state:
            description: State of the application control module
            type: str
            choices:
              - on
              - off
              - inherited
          rule_ids:
            description: List of application control rule IDs
            type: list
            elements: int
  state:
    description:
      - The state the configuration should be left in
      - The state I(gathered) will get the module API configuration from the device
        and transform it into structured data in the format as per the module argspec
        and the value is returned in the I(gathered) key within the result.
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - gathered
      - deleted
author: Ansible Security Automation Team (@justjais) <https://github.com/ansible-security>
"""

EXAMPLES = """
# Using MERGED state
# -------------------

- name: Create DeepSecurity Policy
  trendmicro.deepsec.deepsec_policies:
    state: merged
    config:
      - name: production_policy
        description: "Production server security policy"
        auto_requires_update: "on"
        parent_id: 1
        anti_malware:
          state: "on"
          real_time_scan_configuration_id: 1
        firewall:
          state: "on"
          rule_ids: [1, 2, 3]

- name: Create multiple policies
  trendmicro.deepsec.deepsec_policies:
    state: merged
    config:
      - name: web_server_policy
        description: "Web server policy"
        auto_requires_update: "on"
        firewall:
          state: "on"
        intrusion_prevention:
          state: "on"
      - name: database_policy
        description: "Database server policy"
        auto_requires_update: "on"
        integrity_monitoring:
          state: "on"

# RUN output:
# -----------

#   policies:
#     after:
#     - name: production_policy
#       description: "Production server security policy"
#       id: 10
#       auto_requires_update: "on"
#       parent_id: 1
#       anti_malware:
#         state: "on"
#         real_time_scan_configuration_id: 1
#       firewall:
#         state: "on"
#         rule_ids: [1, 2, 3]
#     before: []

- name: Modify existing policy
  trendmicro.deepsec.deepsec_policies:
    state: merged
    config:
      - name: production_policy
        description: "Updated production policy description"
        firewall:
          state: "off"

# RUN output:
# -----------

#   policies:
#     after:
#     - name: production_policy
#       description: "Updated production policy description"
#       id: 10
#       auto_requires_update: "on"
#       parent_id: 1
#       anti_malware:
#         state: "on"
#         real_time_scan_configuration_id: 1
#       firewall:
#         state: "off"
#     before:
#     - name: production_policy
#       description: "Production server security policy"
#       id: 10
#       auto_requires_update: "on"
#       parent_id: 1
#       anti_malware:
#         state: "on"
#         real_time_scan_configuration_id: 1
#       firewall:
#         state: "on"
#         rule_ids: [1, 2, 3]

# Using REPLACED state
# --------------------

- name: Replace existing Policy
  trendmicro.deepsec.deepsec_policies:
    state: replaced
    config:
      - name: production_policy
        description: "REPLACED production policy"
        auto_requires_update: "off"
        anti_malware:
          state: "off"

# RUN output:
# -----------

#   policies:
#     after:
#     - name: production_policy
#       description: "REPLACED production policy"
#       id: 11
#       auto_requires_update: "off"
#       anti_malware:
#         state: "off"
#     before:
#     - name: production_policy
#       description: "Updated production policy description"
#       id: 10
#       auto_requires_update: "on"
#       parent_id: 1
#       anti_malware:
#         state: "on"
#         real_time_scan_configuration_id: 1
#       firewall:
#         state: "off"

# Using GATHERED state
# --------------------

- name: Gather Policy information by names
  trendmicro.deepsec.deepsec_policies:
    state: gathered
    config:
      - name: production_policy
      - name: web_server_policy

# RUN output:
# -----------

# gathered:
#   - name: production_policy
#     description: "REPLACED production policy"
#     id: 11
#     auto_requires_update: "off"
#     anti_malware:
#       state: "off"
#   - name: web_server_policy
#     description: "Web server policy"
#     id: 12
#     auto_requires_update: "on"
#     firewall:
#       state: "on"
#     intrusion_prevention:
#       state: "on"

- name: Gather ALL policies
  trendmicro.deepsec.deepsec_policies:
    state: gathered

# Using DELETED state
# -------------------

- name: Delete policies
  trendmicro.deepsec.deepsec_policies:
    state: deleted
    config:
      - name: production_policy
      - name: web_server_policy

# RUN output:
# -----------

#   policies:
#     after: []
#     before:
#     - name: production_policy
#       description: "REPLACED production policy"
#       id: 11
#       auto_requires_update: "off"
#       anti_malware:
#         state: "off"
#     - name: web_server_policy
#       description: "Web server policy"
#       id: 12
#       auto_requires_update: "on"
#       firewall:
#         state: "on"
#       intrusion_prevention:
#         state: "on"

# Using OVERRIDDEN state
# ----------------------

- name: Override all policies with new configuration
  trendmicro.deepsec.deepsec_policies:
    state: overridden
    config:
      - name: new_policy
        description: "Only this policy will exist"
        auto_requires_update: "on"
"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
gathered:
  description: The gathered configuration from the device.
  returned: when state is gathered
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
"""
