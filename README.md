# Vib: vi-like browsing

## Motive
When I used normal GUI web browsers, they always felt a little heavy. Chrome had gigabytes of bloat, and Firefox was (and is) still nice for most of my purposes, but when on simpler systems, they felt a little out of place. That's when I discovered [surf](https://surf.suckless.org/) by suckless, and it was good, but I still needed a little bit of customizability. Inspired by Vi keybinds and [DuckDuckGo !bangs](https://duckduckgo.com/bangs), I developed Vib with customizability through the usage of aliases.

## Installation

Firstly, install suckless surf onto your system using your preferred package manager of your choice. In this example, I will be using apt.

```$ sudo apt install surf```

Next, you will have to install vib through [PyPi](https://pypi.org/project/vib-bl/).

If you have not done anything wrong, Vib is now on your computer.

## Usage

```--check-surf``` checks if the surf browser is in your PATH

```--def-rc``` overrides your .vibrc to defaults

```:yt``` prints the URL of the title inserted

check your .vibrc (located at ~/.vibrc) for more details