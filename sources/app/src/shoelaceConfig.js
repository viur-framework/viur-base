import "@viur/shoelace/dist/themes/viur.css"
import "@viur/shoelace/dist/components/button/button.js"
import "@viur/shoelace/dist/components/button-group/button-group.js"
import "@viur/shoelace/dist/components/icon/icon.js"
import "@viur/shoelace/dist/components/input/input.js"
import "@viur/shoelace/dist/components/dropdown/dropdown.js"
import "@viur/shoelace/dist/components/menu/menu.js"
import "@viur/shoelace/dist/components/menu-item/menu-item.js"
import "@viur/shoelace/dist/components/badge/badge.js"
import "@viur/shoelace/dist/components/divider/divider.js"
import "@viur/shoelace/dist/components/avatar/avatar.js"
import "@viur/shoelace/dist/components/dialog/dialog.js"
import "@viur/shoelace/dist/components/tooltip/tooltip.js"
import "@viur/shoelace/dist/components/split-panel/split-panel.js"
import "@viur/shoelace/dist/components/radio-group/radio-group.js"
import "@viur/shoelace/dist/components/radio-button/radio-button.js"
import "@viur/shoelace/dist/components/select/select.js"
import "@viur/shoelace/dist/components/spinner/spinner.js"
import "@viur/shoelace/dist/components/card/card.js"
import "@viur/shoelace/dist/components/tag/tag.js"
import "@viur/shoelace/dist/components/tooltip/tooltip.js"
import "@viur/shoelace/dist/components/checkbox/checkbox.js"
import "@viur/shoelace/dist/components/table-wrapper/table-wrapper.js"
import "@viur/shoelace/dist/components/drawer/drawer.js"
import "@viur/shoelace/dist/components/alert/alert.js"
import "@viur/shoelace/dist/components/icon-button/icon-button.js"
import "@viur/shoelace/dist/components/tree/tree.js"
import "@viur/shoelace/dist/components/tree-item/tree-item.js"
import "@viur/shoelace/dist/components/breadcrumb/breadcrumb.js"
import "@viur/shoelace/dist/components/breadcrumb-item/breadcrumb-item.js"
import '@viur/shoelace/dist/components/format-date/format-date.js';
import '@viur/shoelace/dist/components/format-bytes/format-bytes.js';
import '@viur/shoelace/dist/components/tab-group/tab-group.js';
import '@viur/shoelace/dist/components/tab/tab.js';
import '@viur/shoelace/dist/components/tab-panel/tab-panel.js';


import {setBasePath} from '@viur/shoelace/dist/utilities/base-path.js';
import {registerIconLibrary} from '@viur/shoelace/dist/utilities/icon-library.js';

setBasePath(`/shoelace`)

// Register a custom icons repository for this app

registerIconLibrary("giiix", {
	resolver: (name) => `/icons/${name}.svg`,
	mutator: (svg) => svg.setAttribute("fill", "currentColor"),
});
