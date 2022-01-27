.. _parameters:

Parameters 
==========

Management of the parameters included in configuration files.


.. _parameters-settings-model:

Parameters Settings Model
-------------------------

+-------------+-------------------+-------------------------------------------------------------------+----------------------+----------+
| Field       | Type              | Description                                                       | Example              | Required |
+-------------+-------------------+-------------------------------------------------------------------+----------------------+----------+
| ``source``  | String            | Path of the configuration file that includes the parameter.       | /opt/test.json       | True     |
+-------------+-------------------+-------------------------------------------------------------------+----------------------+----------+
| ``format``  | Enum(json,yaml)   | Format of the configuration file where the parameter is included. | yaml                 | True     |
+-------------+-------------------+-------------------------------------------------------------------+----------------------+----------+
| ``xpath``   | List(String)      | List of keys to indicate the xpath in the configuration file.     | ('agent', 'enabled') | True     |
+-------------+-------------------+-------------------------------------------------------------------+----------------------+----------+
| ``history`` | List(ActionModel) | History of parameter updates.                                     |                      | True     |
+-------------+-------------------+-------------------------------------------------------------------+----------------------+----------+


.. _parameters-output-model:

Parameters Output Model
---------------------

Merge to :ref:`parameters-settings-model` with the following model:
 
+-----------+------+------------------+---------+----------+
| Field     | Type | Description      | Example | Required |
+-----------+------+------------------+---------+----------+
| ``value`` | Any  | Parameter value. | 1.2     | True     |
+-----------+------+------------------+---------+----------+


Read
----

Read the data of all tbe available parameters with the following |REST| call:

.. http:get:: /parameters

    without request body.
    
    The output is a |JSON| dictionary with the following mappings:

    - key: Parameter ID;
    - value: :ref:`parameters-output-model`.

Read a single parameter with the following |REST| call:

.. http:get:: /parameters/{string:id}

    without the request body.

    :param id: indentifies the parameter to read.

    :resheader Content-Type: application/json

    The output is the :ref:`parameters-output-model` in |JSON| format.


Update
------

To update the values of multiple parameters at the same time it is possible to use the following |REST| call:

.. http:post:: /parameters

    with the request body as a |JSON| dictionary with the following mappings:

    - key: Parameter ID;
    - value: any possible value.

    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json

    The output is the a |JSON| dictionary with the following mappings:

    - key: Parameter ID
    - value: :ref:`base-action-model`

To update a single parameter use the following |REST| call:

.. http:post:: /parameters/{string:id}

    with the request body as |JSON| dictionary of any possible value.

    :param id: indentifies the parameter to update.

    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json

    The output is the :ref:`base-action-model` in |JSON| format.

To update a single parameter inline without a request body use the following |REST| call:

.. http:post:: /parameters/{string:id}/{string:value}

    without the request body.

    :param id: indentifies the parameter to update.
    :param value: new value of the parameter.

    :resheader Content-Type: application/json

    The output is the :ref:`base-action-model` in |JSON| format.


.. |JSON| replace:: :abbr:`JSON (JavaScript Object Notation)`
.. |REST| replace:: :abbr:`REST (Representational State Transfer)`
