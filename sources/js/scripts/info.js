export default class Info {
	constructor() {
		this.set("lang", $("html").attr('lang')); //read lang from html Tag
		this.set("isDebug", $("html").hasClass("debug")); //debug is enabled
		this.set("isAdmin", $("html").hasClass("admin")); //admin is enabled

		if (!this.get("isDebug")) {
			console.log("%c%s", "color: red;font-size: 18px;", "Language is " + this.get("lang"));
			console.log("%c%s", "color: red;font-size: 18px;", "Debug mode is enabled");
			console.log("%c%s", "color: red;font-size: 18px;", "Admin mode is "+ ( this.get("isadmin"?"enabled":"disabled")));
		}

	}

	//getter and setter
	set(name, value) {
		this[name] = value;
	}

	get(name) {
		return this[name];
	}

}