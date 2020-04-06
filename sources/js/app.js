import Info from './scripts/info.js'
import Focus from "./scripts/focus.js";

class main {
	constructor() {
		// register starthandler
		document.addEventListener('app-loaded', () => {
			this.loaded()
		})
	}

	load() {
		// init all needed preloads
		console.debug("App init");

		let loaded = new CustomEvent("app-loaded");
		document.dispatchEvent(loaded);
	}

	loaded() { // at this Point Page is ready
		this.infoObj = new Info(); //instantiate a script
		this.focusObj = new Focus();
		console.debug("App loaded");
	}
}

// global Variables
let app;
let timeStart = performance.now();

//main handler
$(document).ready(function () {
	app = new main();
	window.top["app"] = app; // reassign for global usage
	app.load();

	if (app.info.get("isDebug")) {
		let timeEnd = performance.now();
		console.debug("Loaded App in " + (timeEnd - timeStart) + " milliseconds.");
	}
});