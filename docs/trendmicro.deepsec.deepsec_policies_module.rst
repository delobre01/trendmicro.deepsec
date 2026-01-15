.. _trendmicro.deepsec.deepsec_policies_module:


*************************************
trendmicro.deepsec.deepsec_policies
*************************************

**Manages Policy resource module**


Version added: 1.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Policy details for TrendMicro Deep Security.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
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
                        <div>A dictionary of Policy options</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
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
    
    - name: Create DeepSecurity Policy
      trendmicro.deepsec.deepsec_policies:
        state: merged
        config:
          - name: production_policy
            description: "Production server security policy"
            auto_requires_update: true
            parent_id: 1
            anti_malware:
              state: true
              real_time_scan_configuration_id: 1
            firewall:
              state: true
              rule_ids: [1, 2, 3]
    
    - name: Create multiple policies
      trendmicro.deepsec.deepsec_policies:
        state: merged
        config:
          - name: web_server_policy
            description: "Web server policy"
            auto_requires_update: true
            firewall:
              state: true
            intrusion_prevention:
              state: true
          - name: database_policy
            description: "Database server policy"
            auto_requires_update: true
            integrity_monitoring:
              state: true
    
    # RUN output:
    # -----------
    
    #   policies:
    #     after:
    #     - name: production_policy
    #       description: "Production server security policy"
    #       id: 10
    #       auto_requires_update: true
    #       parent_id: 1
    #       anti_malware:
    #         state: true
    #         real_time_scan_configuration_id: 1
    #       firewall:
    #         state: true
    #         rule_ids: [1, 2, 3]
    #     before: []
    
    - name: Modify existing policy
      trendmicro.deepsec.deepsec_policies:
        state: merged
        config:
          - name: production_policy
            description: "Updated production policy description"
            firewall:
              state: false
    
    # RUN output:
    # -----------
    
    #   policies:
    #     after:
    #     - name: production_policy
    #       description: "Updated production policy description"
    #       id: 10
    #       auto_requires_update: true
    #       parent_id: 1
    #       anti_malware:
    #         state: true
    #         real_time_scan_configuration_id: 1
    #       firewall:
    #         state: false
    #     before:
    #     - name: production_policy
    #       description: "Production server security policy"
    #       id: 10
    #       auto_requires_update: true
    #       parent_id: 1
    #       anti_malware:
    #         state: true
    #         real_time_scan_configuration_id: 1
    #       firewall:
    #         state: true
    #         rule_ids: [1, 2, 3]
    
    # Using REPLACED state
    # --------------------
    
    - name: Replace existing Policy
      trendmicro.deepsec.deepsec_policies:
        state: replaced
        config:
          - name: production_policy
            description: "REPLACED production policy"
            auto_requires_update: false
            anti_malware:
              state: false
    
    # RUN output:
    # -----------
    
    #   policies:
    #     after:
    #     - name: production_policy
    #       description: "REPLACED production policy"
    #       id: 11
    #       auto_requires_update: false
    #       anti_malware:
    #         state: false
    #     before:
    #     - name: production_policy
    #       description: "Updated production policy description"
    #       id: 10
    #       auto_requires_update: true
    #       parent_id: 1
    #       anti_malware:
    #         state: true
    #         real_time_scan_configuration_id: 1
    #       firewall:
    #         state: false
    
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
    #     auto_requires_update: false
    #     anti_malware:
    #       state: false
    #   - name: web_server_policy
    #     description: "Web server policy"
    #     id: 12
    #     auto_requires_update: true
    #     firewall:
    #       state: true
    #     intrusion_prevention:
    #       state: true
    
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
    #       auto_requires_update: false
    #       anti_malware:
    #         state: false
    #     - name: web_server_policy
    #       description: "Web server policy"
    #       id: 12
    #       auto_requires_update: true
    #       firewall:
    #         state: true
    #       intrusion_prevention:
    #         state: true
    
    # Using OVERRIDDEN state
    # ----------------------
    
    - name: Override all policies with new configuration
      trendmicro.deepsec.deepsec_policies:
        state: overridden
        config:
          - name: new_policy
            description: "Only this policy will exist"
            auto_requires_update: true
    



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
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when state is gathered</td>
                <td>
                            <div>The gathered configuration from the device.</div>
                    <br/>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ansible Security Team (@ansible-security)



.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

