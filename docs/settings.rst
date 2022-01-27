.. _settings:

Settings
========

The settings of `RESTable` are set in the file `settings.yaml'.

The schema of this file is the following:

+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| Field              | Type            | Description                | Example                           | Required |      |
+====================+=================+============================+===================================+==========+======+
| ``port``           | Integer         | Port where the             | interface is waiting for request. | 9999     | True |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| ``debug``          | Boolean         | Activates the debug.       | True                              | False    |      |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| ``project``        | String          | Project name               | GUARD                             | True     |      |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| ``title``          | String          | Title of the service.      | RESTable Test                     | True     |      |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| ``description``    | String          | Description of the service |                                   | True     |      |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| ``commands``       | Dictionary [1]_ | Available commands         |                                   | False    |      |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| ``configurations`` | Dictionary [2]_ | Available configurations   |                                   | False    |      |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+
| ``parameters``     | Dictionary [3]_ | Available parameters       |                                   | False    |      |
+--------------------+-----------------+----------------------------+-----------------------------------+----------+------+

.. [1] Key: command ID, value: :ref:`commands-settings-model`.
.. [2] Key: configuration ID, value: :ref:`configurations-settings-model`.
.. [3] Key: parameter ID, value: :ref:`parameters-settings-model`.

.. |REST| replace:: :abbr:`REST (Representational State Transfer)`
.. |TCP| replace:: :abbr:`TCP (Transmission Control Protocol)`
