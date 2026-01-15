.. _trendmicro.deepsec.deepsec_scheduled_tasks_module:


********************************************
trendmicro.deepsec.deepsec_scheduled_tasks
********************************************

**Manages Scheduled Task resource module**


Version added: 1.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Scheduled task details for managing security tasks in TrendMicro Deep Security.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of Scheduled Tasks options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Whether the scheduled task is enabled. Searchable as Boolean.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ID of the scheduled task. Searchable as ID.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the scheduled task. Searchable as String.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>recurrence_count</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of times to recur. Searchable as Numeric.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>recurrence_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>once</li>
                                    <li>hourly</li>
                                    <li>daily</li>
                                    <li>weekly</li>
                                    <li>monthly</li>
                        </ul>
                </td>
                <td>
                        <div>Recurrence pattern for the scheduled task. Searchable as Choice.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>schedule_details</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Schedule configuration details for the task.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>start_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Start time for the scheduled task in epoch milliseconds. Searchable as Numeric.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>scan-for-integrity-changes</li>
                                    <li>scan-for-malware</li>
                                    <li>check-for-security-updates</li>
                                    <li>check-for-recommendations</li>
                                    <li>scan-for-open-ports</li>
                                    <li>update-agents</li>
                                    <li>synchronize-directory-server</li>
                                    <li>synchronize-cloud-account</li>
                                    <li>generate-report</li>
                                    <li>run-script</li>
                        </ul>
                </td>
                <td>
                        <div>Type of the scheduled task. Searchable as Choice.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>merged</li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>gathered</li>
                                    <li>deleted</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The state <em>gathered</em> will get the module API configuration from the device and transform it into structured data in the format as per the module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

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



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The configuration as structured data after module completion.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration as structured data prior to module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ansible Security Automation Team (@justjais) <https://github.com/ansible-security>
