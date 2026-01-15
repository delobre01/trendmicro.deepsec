#!/usr/bin/python
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: deepsec_scheduled_tasks
short_description: Manages Scheduled Task resource module
description: Scheduled task details for managing security tasks in TrendMicro Deep Security.
version_added: 1.3.0
options:
  config:
    description: A dictionary of Scheduled Tasks options
    type: list
    elements: dict
    suboptions:
      id:
        description: ID of the scheduled task. Searchable as ID.
        type: int
      name:
        description: Name of the scheduled task. Searchable as String.
        type: str
        required: true
      type:
        description: Type of the scheduled task. Searchable as Choice.
        type: str
        choices:
          - scan-for-integrity-changes
          - scan-for-malware
          - check-for-security-updates
          - check-for-recommendations
          - scan-for-open-ports
          - update-agents
          - synchronize-directory-server
          - synchronize-cloud-account
          - generate-report
          - run-script
      enabled:
        description: Whether the scheduled task is enabled. Searchable as Boolean.
        type: bool
      recurrence_type:
        description: Recurrence pattern for the scheduled task. Searchable as Choice.
        type: str
        choices:
          - once
          - hourly
          - daily
          - weekly
          - monthly
      recurrence_count:
        description: Number of times to recur. Searchable as Numeric.
        type: int
      start_time:
        description: Start time for the scheduled task in epoch milliseconds. Searchable as Numeric.
        type: int
      schedule_details:
        description: Schedule configuration details for the task.
        type: dict
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

- name: Create Scheduled Tasks
  trendmicro.deepsec.deepsec_scheduled_tasks:
    state: merged
    config:
      - name: daily_malware_scan
        type: scan-for-malware
        enabled: true
        recurrence_type: daily
        start_time: 1609459200000
      - name: weekly_integrity_scan
        type: scan-for-integrity-changes
        enabled: true
        recurrence_type: weekly
        start_time: 1609459200000

# RUN output:
# -----------

#   scheduled_tasks:
#     after:
#     - id: 1
#       name: daily_malware_scan
#       type: scan-for-malware
#       enabled: true
#       recurrence_type: daily
#       start_time: 1609459200000
#     - id: 2
#       name: weekly_integrity_scan
#       type: scan-for-integrity-changes
#       enabled: true
#       recurrence_type: weekly
#       start_time: 1609459200000
#     before: []

- name: Modify scheduled task by name
  trendmicro.deepsec.deepsec_scheduled_tasks:
    state: merged
    config:
      - name: daily_malware_scan
        enabled: false

# RUN output:
# -----------

#   scheduled_tasks:
#     after:
#     - id: 1
#       name: daily_malware_scan
#       type: scan-for-malware
#       enabled: false
#       recurrence_type: daily
#       start_time: 1609459200000
#     before:
#     - id: 1
#       name: daily_malware_scan
#       type: scan-for-malware
#       enabled: true
#       recurrence_type: daily
#       start_time: 1609459200000

# Using REPLACED state
# --------------------

- name: Replace existing Scheduled Task
  trendmicro.deepsec.deepsec_scheduled_tasks:
    state: replaced
    config:
      - name: daily_malware_scan
        type: check-for-security-updates
        enabled: true
        recurrence_type: hourly
        recurrence_count: 6
        start_time: 1609459200000

# RUN output:
# -----------

#   scheduled_tasks:
#     after:
#     - id: 3
#       name: daily_malware_scan
#       type: check-for-security-updates
#       enabled: true
#       recurrence_type: hourly
#       recurrence_count: 6
#       start_time: 1609459200000
#     before:
#     - id: 1
#       name: daily_malware_scan
#       type: scan-for-malware
#       enabled: false
#       recurrence_type: daily
#       start_time: 1609459200000

# Using GATHERED state
# --------------------

- name: Gather Scheduled Tasks by names
  trendmicro.deepsec.deepsec_scheduled_tasks:
    state: gathered
    config:
      - name: daily_malware_scan
      - name: weekly_integrity_scan

# RUN output:
# -----------

# gathered:
#   - id: 1
#     name: daily_malware_scan
#     type: scan-for-malware
#     enabled: true
#     recurrence_type: daily
#     start_time: 1609459200000
#   - id: 2
#     name: weekly_integrity_scan
#     type: scan-for-integrity-changes
#     enabled: true
#     recurrence_type: weekly
#     start_time: 1609459200000

- name: Gather ALL Scheduled Tasks
  trendmicro.deepsec.deepsec_scheduled_tasks:
    state: gathered

# Using DELETED state
# -------------------

- name: Delete Scheduled Tasks
  trendmicro.deepsec.deepsec_scheduled_tasks:
    state: deleted
    config:
      - name: daily_malware_scan
      - name: weekly_integrity_scan

# RUN output:
# -----------

#   scheduled_tasks:
#     after: []
#     before:
#     - id: 1
#       name: daily_malware_scan
#       type: scan-for-malware
#       enabled: true
#       recurrence_type: daily
#       start_time: 1609459200000
#     - id: 2
#       name: weekly_integrity_scan
#       type: scan-for-integrity-changes
#       enabled: true
#       recurrence_type: weekly
#       start_time: 1609459200000
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
"""
