#!/usr/bin/python
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: deepsec_directory_lists
short_description: Manages Directory List resource module
description: Directory lists used for scan inclusion/exclusion.
version_added: 1.2.0
options:
  config:
    description: A dictionary of Directory List options
    type: list
    elements: dict
    suboptions:
      name:
        description: Name of the directory list. Searchable as String.
        type: str
      description:
        description: Description of the directory list. Searchable as String.
        type: str
      items:
        description: Directory paths in the list.
        type: list
        elements: str
      id:
        description: ID of the directory list. Searchable as ID.
        type: int
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

- name: Create Directory Lists
  trendmicro.deepsec.deepsec_directory_lists:
    state: merged
    config:
      - name: test_directory_list_1
        description: Directory list 1 for scan exclusion
        items:
          - /tmp/exclude1
          - /var/log/exclude1
      - name: test_directory_list_2
        description: Directory list 2 for scan inclusion
        items:
          - /home/include1
          - /opt/include1

# RUN output:
# -----------

#   directory_lists:
#     after:
#     - description: Directory list 1 for scan exclusion
#       id: 1
#       items:
#       - /tmp/exclude1
#       - /var/log/exclude1
#       name: test_directory_list_1
#     - description: Directory list 2 for scan inclusion
#       id: 2
#       items:
#       - /home/include1
#       - /opt/include1
#       name: test_directory_list_2
#     before: []

- name: Modify the items of Directory List by name
  trendmicro.deepsec.deepsec_directory_lists:
    state: merged
    config:
      - name: test_directory_list_1
        items:
          - /tmp/exclude1
          - /var/log/exclude1
          - /tmp/exclude2

# RUN output:
# -----------

#   directory_lists:
#     after:
#     - description: Directory list 1 for scan exclusion
#       id: 1
#       items:
#       - /tmp/exclude1
#       - /var/log/exclude1
#       - /tmp/exclude2
#       name: test_directory_list_1
#     before:
#     - description: Directory list 1 for scan exclusion
#       id: 1
#       items:
#       - /tmp/exclude1
#       - /var/log/exclude1
#       name: test_directory_list_1

# Using REPLACED state
# --------------------

- name: Replace existing Directory Lists
  trendmicro.deepsec.deepsec_directory_lists:
    state: replaced
    config:
      - name: test_directory_list_1
        description: REPLACED Directory list 1
        items:
          - /tmp/replaced1
          - /var/replaced1

# RUN output:
# -----------

#   directory_lists:
#     after:
#     - description: REPLACED Directory list 1
#       id: 3
#       items:
#       - /tmp/replaced1
#       - /var/replaced1
#       name: test_directory_list_1
#     before:
#     - description: Directory list 1 for scan exclusion
#       id: 1
#       items:
#       - /tmp/exclude1
#       - /var/log/exclude1
#       - /tmp/exclude2
#       name: test_directory_list_1

# Using OVERRIDDEN state
# ----------------------

- name: Override all Directory Lists
  trendmicro.deepsec.deepsec_directory_lists:
    state: overridden
    config:
      - name: test_directory_list_override
        description: Override directory list
        items:
          - /override/path1

# RUN output:
# -----------

#   directory_lists:
#     after:
#     - description: Override directory list
#       id: 4
#       items:
#       - /override/path1
#       name: test_directory_list_override
#     before:
#     - description: REPLACED Directory list 1
#       id: 3
#       items:
#       - /tmp/replaced1
#       - /var/replaced1
#       name: test_directory_list_1
#     - description: Directory list 2 for scan inclusion
#       id: 2
#       items:
#       - /home/include1
#       - /opt/include1
#       name: test_directory_list_2

# Using GATHERED state
# --------------------

- name: Gather Directory Lists by names
  trendmicro.deepsec.deepsec_directory_lists:
    state: gathered
    config:
      - name: test_directory_list_1
      - name: test_directory_list_2

# RUN output:
# -----------

# gathered:
#   - description: Directory list 1 for scan exclusion
#     id: 1
#     items:
#     - /tmp/exclude1
#     - /var/log/exclude1
#     name: test_directory_list_1
#   - description: Directory list 2 for scan inclusion
#     id: 2
#     items:
#     - /home/include1
#     - /opt/include1
#     name: test_directory_list_2

- name: Gather ALL of the Directory Lists
  trendmicro.deepsec.deepsec_directory_lists:
    state: gathered

# Using DELETED state
# -------------------

- name: Delete Directory Lists
  trendmicro.deepsec.deepsec_directory_lists:
    state: deleted
    config:
      - name: test_directory_list_1
      - name: test_directory_list_2
# RUN output:
# -----------

#   directory_lists:
#     after: []
#     before:
#     - description: Directory list 1 for scan exclusion
#       id: 1
#       items:
#       - /tmp/exclude1
#       - /var/log/exclude1
#       name: test_directory_list_1
#     - description: Directory list 2 for scan inclusion
#       id: 2
#       items:
#       - /home/include1
#       - /opt/include1
#       name: test_directory_list_2
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
