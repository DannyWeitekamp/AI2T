# AI2T

The AI2T agent library: a general interface for training agents via
demonstration and feedback. AI2T began as a fork of the Apprentice Learner
(AL_Core) project and has since diverged from it.

The HTTP server that exposes AI2T agents lives in a separate repository,
AI2T_AgentServer.

# Installation

```bash
git clone https://github.com/DannyWeitekamp/AI2T
cd AI2T
python3 -m pip install -r requirements.txt
python3 -m pip install -e .
```

# Tic Tac Toe Example
This example is a simple command line app where you can train a single agent to take legal Tic Tac Toe moves against itself. One of the main benefits of this example is the ability to try out different types of agents and confirm they all work without errors.

```bash
python3 examples/tic-tac-toe.py
```

Follow the on screen prompts to train the agent to take moves.

To try out different types of agents you can provide a different value for the -agent argument:

```bash
python3 examples/tic-tac-toe.py -agent Modular
```


# Papers and Other Documentation
1. Chris’s Thesis [link](http://christopia.net/thesis) specifically Chapter 3
    * Probably the best current source on the framework in writing
2. The Apprentice Learner Architecture EDM paper [link](http://erikharpstead.net/papers/C9%20-%20MacLellan%20et%20al.%20-%202016%20-%20Apptentice%20Learner%20Architecture%20EDM%20Conference.pdf)
    * The best published reference, but the model diagram in this one is outdated
3. The TRESTLE Algorithm [link](http://erikharpstead.net/papers/J1%20-%20MacLellan%20et%20al.%20-%202016%20-%20TESTLE%20-%20ACS%20Journal.pdf)
    * Describes TRESTLE
4. TRESTLE docs [link](https://concept-formation.readthedocs.io/en/latest/)
    * The documentation for the actual TRESTLE software library, these are generally more accurate than the published papers but nothing has substantially changed (e.g., we technically calculate category utility differently now but in a way that produces the exact same behavior with less computation)
    * This is also useful to check out because we use the preprocessors from this library throughout AI2T to do things like flatten states for processing.
5. Py Search Docs [link](https://py-search.readthedocs.io/en/latest/)
    * The search library that Chris wrote that is used throughout AI2T/trestle

