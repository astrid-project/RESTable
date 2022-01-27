.. _configurations:

Configurations 
==============

Management of the configuration files.


.. _configurations-settings-model:

Configurations Settings Model
-------------------------

+-------------+-------------------+-----------------------------------+----------------+----------+
| Field       | Type              | Description                       | Example        | Required |
+-------------+-------------------+-----------------------------------+----------------+----------+
| ``path``    | String            | Path of the configuration file.   | /opt/test.json | True     |
+-------------+-------------------+-----------------------------------+----------------+----------+
| ``format``  | Enum(json,yaml)   | Format of the configuration file. | yaml           | True     |
+-------------+-------------------+-----------------------------------+----------------+----------+
| ``history`` | List(ActionModel) | History of configuration updates. |                | True     |
+-------------+-------------------+-----------------------------------+----------------+----------+


.. _configurations-output-model:

Configurations Output Model
---------------------------

Merge to :ref:`configurations-settings-model` with the following model:

+-------------+------+--------------------------------+---------+----------+
| Field       | Type | Description                    | Example | Required |
+-------------+------+--------------------------------+---------+----------+
| ``content`` | Any  | Content of configuration file. |         | True     |
+-------------+------+--------------------------------+---------+----------+


Read
----

Read the data of all tbe available configurations with the following |REST| call:

.. http:get:: /configurations

    without request body.
    
    The output is a |JSON| dictionary with the following mappings:

    - key: Configuration ID;
    - value: :ref:`configurations-output-model`.

Read a single configuration with the following |REST| call:

.. http:get:: /configurations/{string:id}

    without the request body.

    :param id: indentifies the configuration to read.

    :resheader Content-Type: application/json

    The output is the :ref:`configurations-output-model` in |JSON| format.


Update
------

To update the values of multiple configurations at the same time it is possible to use the following |REST| call:

.. http:post:: /configurations

    with the request body as a |JSON| dictionary with the following mappings:

    - key: Configuration ID;
    - value: any possible value.

    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json

    The output is the a |JSON| dictionary with the following mappings:

    - key: Configuration ID
    - value: :ref:`base-action-model`

To update a single configuration use the following |REST| call:

.. http:post:: /configurations/{string:id}

    with the request body as |JSON| dictionary of any possible value.

    :param id: indentifies the configuration to update.

    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json

    The output is the :ref:`base-action-model` in |JSON| format.


.. |JSON| replace:: :abbr:`JSON (JavaScript Object Notation)`
.. |REST| replace:: :abbr:`REST (Representational State Transfer)`
