Welcome to Fakernaija's Documentation!
======================================

Overview
--------

**Fakernaija** is a Python library designed to help developers generate realistic Nigerian-specific data. So when you just need some random Nigerian data to spice up your project, Fakernaija can help you generate random data to meet your requirements, including a CLI for easy data exports.

.. toctree::
   :hidden:
   :maxdepth: 1

   Home <self>
   installation
   guide
   internals

Features
--------

- Generate culturally accurate Nigerian data — no more random names that don't make sense!
- Generate data quickly from the terminal with our CLI commands, because who has time to waste?
- Export data to JSON, CSV, and plain text formats, like wrapping suya in your preferred package.
- Integrate easily into your Python projects, like Made-in-Aba shoes that fit perfectly.

Installation
------------

Fakernaija can be easily installed using pip, so let's get you started in no time:

.. code-block:: bash

   pip install -U fakernaija

For more detailed instructions, please refer to the :doc:`installation` guide.

Getting Started
---------------

To start using Fakernaija in your project, here is a simple example you can run via your Python shell:

.. code-block:: python

   >>> from fakernaija import Faker

   >>> naija = Faker()

   >>> print("A random Nigerian full name:", naija.full_name())
   A random Nigerian full name: Ololade Lawal

There's more, so check out the :doc:`guide` section. No yawa, we've got you.

Command Line Interface (CLI)
----------------------------

Fakernaija comes with a CLI to generate data directly from your terminal. For example:

.. code-block:: bash

   $ naija email --domain unn.edu.ng --tribe igbo --gender female --repeat 3
   maduike.ugochi@unn.edu.ng
   somtochi.mbakwe@unn.edu.ng
   mmasinwodo25@unn.edu.ng

Refer to the :doc:`commands` section for more CLI commands and options.

API Reference
-------------

The API reference section provides documentation on the various modules and classes available in the Fakernaija library. Below are the key components of the API:

- :doc:`faker`: This module serves as the primary interface for generating various types of data. It aggregates multiple mixins to provide a wide range of functionalities.

- :doc:`mixins`: The mixins are specialized classes that handle specific data generation tasks.

- :doc:`commands`: Documentation on Fakernaija's Command Line Interface (CLI) commands, explaining how to generate data directly from your terminal and export it in different formats.

- :doc:`providers`: These are the data providers which interfaces with the Mixins to generate data.

.. toctree::
   :caption: API Reference
   :maxdepth: 1
   :hidden:

   faker
   mixins
   commands
   providers

Get Involved
------------

If you're interested in contributing to Fakernaija, this section will guide you through the development process. The key sections are:

- :doc:`contributing`: No be beans, but we've made it as easy as possible to contribute to the library.

- :doc:`documentation`: If writing docs is your thing, this guide shows you what to do.

- :doc:`testing`: Skipping tests is like serving jollof without seasoning — not quite right.

- :doc:`deployment`: A guide to deploying new versions of the library on PyPI.

.. toctree::
   :caption: Development
   :maxdepth: 1
   :hidden:

   contributing
   documentation
   testing
   deployment

Meta
----

This section provides information related to the project itself:

- :doc:`changelog`: Think of this as our `Before and After` story — how we've grown and improved.

- :doc:`support`: No need to shout `Epp me!` — we've got your back if you are stuck.

- :doc:`credits`: We believe in giving `Kudos` where it's due. After all, who no like better thing?

- :doc:`license`: Just like free Wi-Fi, our ``MIT License`` makes it available for everyone to enjoy.

.. toctree::
   :caption: Meta
   :maxdepth: 1
   :hidden:

   changelog
   support
   credits
   license
