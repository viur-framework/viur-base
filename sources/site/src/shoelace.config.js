// sl css variables
import '@viur/shoelace/dist/themes/light.css';
//import '@viur/shoelace/dist/themes/viur.css';
import '@viur/shoelace/dist/components/alert/alert.js';
import '@viur/shoelace/dist/components/back-to-top/back-to-top.js';
import '@viur/shoelace/dist/components/bar/bar.js';
import '@viur/shoelace/dist/components/breadcrumb/breadcrumb.js';
import '@viur/shoelace/dist/components/breadcrumb-item/breadcrumb-item.js';
import '@viur/shoelace/dist/components/button/button.js';
import '@viur/shoelace/dist/components/button-group/button-group.js';
import '@viur/shoelace/dist/components/icon-button/icon-button.js';
import '@viur/shoelace/dist/components/card/card.js';
import '@viur/shoelace/dist/components/color-picker/color-picker.js';
import '@viur/shoelace/dist/components/carousel/carousel.js';
import '@viur/shoelace/dist/components/carousel-item/carousel-item.js';
import '@viur/shoelace/dist/components/details/details.js';
import '@viur/shoelace/dist/components/details-group/details-group.js';
import '@viur/shoelace/dist/components/dialog/dialog.js';
import '@viur/shoelace/dist/components/dropdown/dropdown.js';
import '@viur/shoelace/dist/components/icon/icon.js'; // For SlSelect, SlAlert
import '@viur/shoelace/dist/components/icon-button/icon-button.js'; // For SlSelect, SlAlert
import '@viur/shoelace/dist/components/menu/menu.js';
import '@viur/shoelace/dist/components/menu-item/menu-item.js';
import '@viur/shoelace/dist/components/rating/rating.js';
import '@viur/shoelace/dist/components/option/option.js'; // For SlSelect
import '@viur/shoelace/dist/components/select/select.js';
import '@viur/shoelace/dist/components/skeleton/skeleton.js';
import '@viur/shoelace/dist/components/switch/switch.js';
import '@viur/shoelace/dist/components/spinner/spinner.js';
import '@viur/shoelace/dist/components/split-panel/split-panel.js';
import '@viur/shoelace/dist/components/tab-group/tab-group.js';
import '@viur/shoelace/dist/components/tab-panel/tab-panel.js';
import '@viur/shoelace/dist/components/tab/tab.js';
import '@viur/shoelace/dist/components/tag/tag.js';
import '@viur/shoelace/dist/components/tree/tree.js';
import '@viur/shoelace/dist/components/tree-item/tree-item.js';
import '@viur/shoelace/dist/components/tooltip/tooltip.js';
import '@viur/shoelace/dist/components/combobox/combobox.js';
import '@viur/shoelace/dist/components/range/range.js';
import '@viur/shoelace/dist/components/multi-range/multi-range.js';
import '@viur/shoelace/dist/components/format-number/format-number.js';

// Form-elements
import "@viur/shoelace/dist/components/divider/divider.js";
import "@viur/shoelace/dist/components/input/input.js";
import "@viur/shoelace/dist/components/textarea/textarea.js";
import '@viur/shoelace/dist/components/checkbox/checkbox.js';
import '@viur/shoelace/dist/components/radio/radio.js';
import '@viur/shoelace/dist/components/radio-group/radio-group.js';



import { setBasePath, getBasePath } from '@viur/shoelace/dist/utilities/base-path'
import { registerIconLibrary } from '@viur/shoelace/dist/utilities/icon-library.js'

setBasePath(`/app/shoelace`)

registerIconLibrary('icons', {
    resolver: name => `/app/icons/${name}.svg`,
    mutator: svg => svg.setAttribute('fill', 'currentColor'),
})

registerIconLibrary('logos', {
    resolver: name => `/app/logos/${name}.svg`,
})

export async function allDefinedShoelace(options) {
  const opts = {
    match: (tagName) => tagName.startsWith("sl-"),
    additionalElements: [],
    root: document,
    ...options,
  }
  const additionalElements = Array.isArray(opts.additionalElements)
    ? opts.additionalElements
    : [opts.additionalElements]
  const undefinedElements = [...opts.root.querySelectorAll(":not(:defined)")]
    .map((el) => el.localName)
    .filter((tag, index, arr) => arr.indexOf(tag) === index)
    .filter((tag) => opts.match(tag))
  const tagsToAwait = [...undefinedElements, ...additionalElements]
  await Promise.all(tagsToAwait.map((tag) => customElements.whenDefined(tag)))
  await new Promise(requestAnimationFrame)
}
