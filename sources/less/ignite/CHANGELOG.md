# Change Log
All notable changes to this project will be documented in this file.

## [develop]


## [4.0.0] - 2021-02-26

### Changed
- **BREAKING:** changed many variables of basic and generic elements (see deprecated.less for more)
- **BREAKING:** changed names of generic elements mixins to `.generic{Name}()` – e.g. `.genericBtn()` instead of `.btn()` 
- improved flex behaviour of inputs and selects
- `.shd` and `.txt-shd` are now normal css elements - no longer mixins and use the _@defaultShadowColor_
- moved basic input resets to reset.less
- increased mobile font-size of generic tables.
- made some (form and button) alignments more intuitive
- standardised `.basicTickbox()` and `.basicInput()`
- made `margin-bottom` of `.genericMsg` conditional
- adjusted screen sizes
- many small changes and adjustments
- some styling changes

### Added
- **BREAKING:** added prefixed variables to all generic elements
- **BREAKING:** added mixins with parentheses to all generic elements (you need to configure/activate them manually now)
- added more customisation options to generic elements
- added `max-width` to inputs and selects
- added folder overviews (_foundation.less, _generic.less, _mixins.less)
- added better support for and hooks to inputvalidation.less and basicinput.less
- added important mobility to `.{bar}-items` (left, center, right modifier).
- **NEW** popup.less: a popup container that appears above other content onscreen
- **NEW** popout.less: a popout container that emerges from a location with an arrow pointing at it
- **NEW** box.less: a visible multi-purpose container (head/body/foot), which can group other elements.
- **NEW** deprecated.less: deprecated variables are redirected to their successors or a viable default
- **NEW** `@spaceSmall`, `@spaceMedium`, `@spaceLarge` too better coordinate space between different objects.
- **NEW** cascading `.{input-groups}` are now supported
- **NEW** `.{input-group}-items` and their modifiers help to style (cascading) `.{input-groups}`

### Removed
- removed old browser support from reset.less
- Let the guards down: removed guards from generic elements and colorize mixins (see deprecated.less for more)
- removed `white-space: nowrap;` from `.genericLabel()`


## [3.2.0] - 2020-01-24

### Added
- XXL support for font size and break points
- missing color to select
- missing font-weight to textarea
- default value to .order


## [3.1.0] - 2019-05-03

### Changed
- comments to a consistent notation
- moved selections from state.less to basic.less
- moved media queries from state.less to mediaqueries.less
- burger: new cascade. class `{burger}--to-cross` is now related to the same element with class `{burger}` 
- padding of lists (ul/ol with `.is-list`)
- table-width is not full-sized (100%) by default

### Fixed
- several typos and syntax and improved readability
- color of border-bottom in last row of a table
- use @input… classes as default values for basicInput-mixin

### Removed
- NPM Packages and Gulpfile. Ignite should be only a library.
- camelCase in table class names (btnGroup, optionGroup, -vSmall etc.)
- removed state.less


## [3.0.0] - 2018-09-24

After more than a year of development Ignite 3.0.0 now serves as a less foundation library.
Put it into any project for a solid boiler plate.
Functions and output file size have been reduced to the bare minimum.
You have to opt-in and initialize functions to use them.

### Added
- all generic components are now guarded: you have to opt-in
- border mixin is now used in generic components

### Changed
- folders have been restructured 
- »tools« renamed to »mixins«
- gulpfile changed to adopt the new folder structure
- moved utility functions to the corresponding mixin less files (e.g. .shd() to shadow.less) 
- moved .basicInput() to its own less file
- more undocumented changes
- version syntax from "-v" to "--" (&-vSmall is now &--small)

### Removed
- grid.less has been removed, please use display: grid;  
- util.less has been removed
- cleaned up some obsolete vendor prefixes
- camelCase in class names (btnGroup, optionGroup, -vSmall etc.)

## [2.0.0] - 2016-12-19

In this major release ViUR Ignite CSS starts using the mobile first paradigm.

This means some huge changes to the way media queries are handled.
With 2.0.0 just use classes with .mq- prefix.
They are stored within mediaqueries.less and can be stacked (min + max + orientation).
The gulp task merges all media queries to the end of the compiled css file.

Moreover flex layout is no longer the exception but the norm.


## [1.0.24] - 2016-08-16
### Added
- menu variation .menu-vRow
- single element spinner: .single-spinner
- single-spinner support for buttons and menu-links
- :focus states for inputs
- .switch (boolean selection)
- .radio buttons (single selection)
- .check boxes (multiple selection)
- .optionGroup to arrange radios and checks
- .optionGroup-vSelectionList to style radio and check groups as scrollable list
- NESW positioning for .popup element
- util.less elements: text transforms, repsosive format, show/hiding class
- image shapes (rounded, circle, thumbnail)
- .thumnail
- cite element to .blockquote
- kbd (key) element
- added support for .input-vBlock and .textarea-vBlock next to a label (inline)
- table.less: no-border variations
- build task:
	- stylefmt for the correct syntax
	- sourcemap support
	- support for /* ... */ comments in style.css
- Small and large modifier for .popup element

### Changed
- using .menuWrapper for mobile menu instead of .sidebar
- some responsive behaviour of form elements for increased consistency
- now each element is border-box: box-sizing (before there were some exceptions)
- .shd, .center (X, Y), .pointer are now native css classes so you can use those as mixin and in html
- restyled pre/code element
- grid sizes/offsets (third, quarter)
- redrawn headlines/sublines
- .popup-content and .popup-footer now use em instead of rem in font-size
- .content now uses min-width:0; instead of overflow:hidden;
- .single-spinner is now smaller

### Deprecated
- .formActions are deprecated: please use the .bar element instead

### Fixed
- double scroller
- namespacing for tabs (styling affected radio buttons)
- .popup now has a max-height and proper content scrollbars
- .barGroup-vRight and .barGroup-vCenter now float correctly


## [1.0.23] - 2016-07-31
### Added
- center-functions [.center(), .centerX().centerY()]
- key element: a container to present key visuals, claims or slogans
- bar element: for vertical alignment and horizontal distribution, such as navigation bars or inline forms
- pagination
- tab variation: tab-vFullscreen

### Changed
- monoFont to 'Source Code Pro'
- .tab label is now called .tab-label to increase the sturdiness
- .media-image.small is now called .media-image.media-image-vSmall to increase consistency
- breadcrumb items are now namespaced

### Fixed
- placeholder.svg is now linked correctly in image.less
- Tabs work again


## [1.0.22] - 2016-07-28
### Removed
- removed doc styles


## [1.0.21] - 2016-07-24
### Added
- several slider styles


## [1.0.20] - 2016-07-23
- Changelog started here


[4.0.0]: https://github.com/viur-framework/ignite/compare/3.2.0...4.0.0
[3.2.0]: https://github.com/viur-framework/ignite/compare/3.1.0...3.2.0
[3.1.0]: https://github.com/viur-framework/ignite/compare/3.0.00...3.1.0
[3.0.0]: https://github.com/viur-framework/ignite/compare/1.0.24...3.0.00
[2.0.0]: https://github.com/viur-framework/ignite/compare/1.0.24...2.0.00
[1.0.24]: https://github.com/viur-framework/ignite/compare/1.0.23...1.0.24
[1.0.23]: https://github.com/viur-framework/ignite/compare/1.0.22...1.0.23
[1.0.22]: https://github.com/viur-framework/ignite/compare/1.0.21...1.0.22
[1.0.21]: https://github.com/viur-framework/ignite/compare/1.0.20...1.0.21
[1.0.20]: https://github.com/viur-framework/ignite/compare/02a8706fb892b091bfa913d3194736a5d5a1ef4a...1.0.20
