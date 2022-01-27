.. _commands:

Commands 
========

Management of the commands.


.. _commands-settings-model:

Commands Settings Model
-----------------------

+-------------+-------------------+--------------------------------------------------------------+---------+----------+
| Field       | Type              | Description                                                  | Example | Required |
+-------------+-------------------+--------------------------------------------------------------+---------+----------+
| ``script``   | String            | Command to be executed.                                      | True    | True     |
+-------------+-------------------+--------------------------------------------------------------+---------+----------+
| ``daemon``  | Boolean           | Indicate if the command has to be executed as daemon or not. | True    | False    |
+-------------+-------------------+--------------------------------------------------------------+---------+----------+
| ``history`` | List(ActionModel) | History of command execution.                                |         | True     |
+-------------+-------------------+--------------------------------------------------------------+---------+----------+


.. _commands-output-model:

Commands Output Model
---------------------

Identical to :ref:`commands-settings-model`. 


Read
----

Read the data of all tbe available commands with the following |REST| call:

.. http:get:: /commands

    without request body.
    
    The output is a |JSON| dictionary with the following mappings:

    - key: Command ID;
    - value: :ref:`commands-output-model`.

Read a single command with the following |REST| call:

.. http:get:: /commands/{string:id}

    without request body.

    :param id: indentifies the command to read.

    :resheader Content-Type: application/json

    The output is the :ref:`commands-output-model` in |JSON| format.


Execute
-------

To execute all the available commands at the same time it is possible to use the following |REST| call:

.. http:post:: /commands

    without the request body.

    :resheader Content-Type: application/json

    The output is the a |JSON| dictionary with the following mappings:

    - key: Command.ID
    - value: :ref:`base-action-model`

To execute a single command use the following |REST| call:

.. http:post:: /commands/{string:id}

    without the request body.

    :param id: indentifies the command to execute.

    :resheader Content-Type: application/json

    The output is the :ref:`base-action-model` in |JSON| format.


.. |JSON| replace:: :abbr:`JSON (JavaScript Object Notation)`
.. |REST| replace:: :abbr:`REST (Representational State Transfer)`
