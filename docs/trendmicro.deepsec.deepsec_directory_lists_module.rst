.. _trendmicro.deepsec.deepsec_directory_lists_module:


******************************************
trendmicro.deepsec.deepsec_directory_lists
******************************************

**Manages Directory List resource module**


Version added: 1.2.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Directory lists used for scan inclusion/exclusion.




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
                        <div>A dictionary of Directory List options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of the directory list. Searchable as String.</div>
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
                        <div>ID of the directory list. Searchable as ID.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Directory paths in the list.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the directory list. Searchable as String.</div>
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
