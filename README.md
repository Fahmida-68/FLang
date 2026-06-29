# FLang

FLang is a lightweight, procedural toy programming language built from scratch using Python. It features a complete custom compiler architecture (Lexer, Parser, and Interpreter) and an interactive, stylized in-browser playground.
Inspired by modern localized languages, FLang maps traditional program structures into a minimal, expressive, and fun runtime ecosystem.


## Core Features
* Full Compiler Pipeline: Includes custom Lexical Analysis, Syntax Parsing (AST), and a Core Runtime Interpreter.
* Interactive Playground: A sleek, fully dark-themed browser editor to write, run, and clear your code instantly.
* Dynamic Control Flow: Full support for variable initialization, standard print outputs, conditional logic, and iterative loop blocks.


## Architecture Blueprint
The repository is structured around standard compiler design design-patterns:

* `tokens.py` - Vocabulary mapping holding keyword structures and literal definitions.
* `lexer.py` - Tokenizer engine breaking down raw string inputs into processable syntactic elements.
* `parser.py` - Grammatical syntax analyzer enforcing rule blocks and structure validation.
* `interpreter.py` - The core engine executing the validated parse trees and managing abstract memory allocation.
* `main.py` - Central coordination connector script handling input files and compiler sequences.
* `index.html` - The modern, front-facing UI layout built for seamless client-side visual testing.

---

## Sample Syntax Guide

Here is a standard example showing variables, loops, and standard matching patterns in FLang:

```flang
shuru flang
    bol "Hello World"
    
    rakho a = 3
    rakho b = 0

    jotokkhon (b < 5) {
        bol b

        jodi (b == a) {
            bol "b is equal to a"
        } natho (b == 0) {
            bol "b is equal to zero"
        }

        b = b + 1
    }
shesh flang



## How to Run Locally

Since the playground ecosystem is fully standalone, you do not need any complex setup:
1. Clone or download this repository.
2. Double-click or open `index.html` directly inside any modern web browser.
3. Write your code inside the editor block and click **Run** to execute!


## Developer Info
* Project Maintainer: Antana Fahmida
* Contact Email: [antanafahmida2013@gmail.com](mailto:antanafahmida2013@gmail.com)
* GitHub Repository [https://github.com/Fahmida-68/FLang](https://github.com/Fahmida-68/FLang)