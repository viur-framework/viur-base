[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://raw.githubusercontent.com/viur-ignite/ignite/master/LICENSE)

# Ignite
> ViUR Ignite is a sturdy boilerplate css framework 

Our goal is to create a framework that is sturdy and scalable 
yet lightweight and adaptable to our different customer projects.
Our approach to CSS is influenced by many modern CSS principles: object oriented, functional and structured.
It uses the power of LESS preprocessing (mixins, variables, cascading etc.) and CSS3+. 

For a detailed introduction and examples have a look at [ignite.viur.dev](https://ignite.viur.dev).

## What is this framework for?
* Ignite is a development toolkit for sturdy HTML and CSS
* It is a lightweight collection of helpful CSS components
* It is responsive and adaptable
* It is built with LESS

## Foundation
* _appconf.less_ – stores all default variables and constants.
* _basic.less_ – styling of all application basics (body, fonts, headlines, lists etc.).
* _reset.less_ – resets all browsers to the same base state.
* _deprecated.less_ – lists deprecated variables and redirectes them to their successors or a viable default.

## Generic application elements
* _bar.less_ – a multi-purpose horizontal level, which can contain other elements.
* _burger.less_ – a common menu burger: three horizontal lines that open your hidden menu.
* _button.less_ – a simple button with a complex feature set (hover, active, disabled, busy, different sizes and more).
* _form.less_ – all common form elements (inputs, labels, selects, textareas, grouping etc.).
* _icon.less_ – proper sizing and coloring for inline SVG icons used in buttons or other elements.
* _message.less_ – a simple message template used for alerts, hints, errors, warnings etc.
* _popout.less_ – a popout container that emerges from a location with an arrow pointing at it.
* _popup.less_ – a popup container that appears above other content onscreen.
* _table.less_ – a classic table layout.
* _wrap.less_ – a basic collection of page wrappers.

## LESS mixins
* _basicInput.less_ – makes all your buttons, selects and inputs look alike.
* _border.less_ – helps with `border` and `border-radius`.
* _inputvalidation.less_ – unifies all graphical validation feedback for selects and inputs.
* _mediaqueries.less_ – is a really simple solution for media queries.
* _order.less_ – unifies `order` in flexbox layouts.
* _position.less_ – simple helper mixins for object positioning.
* _shadow.less_ – adds complex shadows to achieve different levels of depth for material designs.
* _svg.less_ – stores a collection of useful inline SVG backgrounds used by Ignite.
* _zindex.less_ – organizes and unifies `zindex` across the whole application.

---

## Usage

**Submodule**

We recommend to add ignite as a submodule in your project:
```bash
git submodule add git@github.com:viur-framework/ignite.git
```
or
```bash
git submodule add https://github.com/viur-framework/ignite.git
```

**LESS Import**

Then you can import ignite in your projects style.less
```less
@import "ignite/ignite";
```

---

## Contribution guidelines
* Available for use under the GPL-3.0 license

---

## Who do I talk to?
* [@phneutral](https://github.com/phneutral)
* [@sveneberth](https://github.com/sveneberth)
