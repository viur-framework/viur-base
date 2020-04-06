"use strict";

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var Info = /*#__PURE__*/function () {
  function Info() {
    _classCallCheck(this, Info);

    this.set("lang", $("html").attr('lang')); //read lang from html Tag

    this.set("isDebug", $("html").hasClass("debug")); //debug is enabled

    this.set("isAdmin", $("html").hasClass("admin")); //admin is enabled

    if (!this.get("isDebug")) {
      console.log("%c%s", "color: red;font-size: 18px;", "Language is " + this.get("lang"));
      console.log("%c%s", "color: red;font-size: 18px;", "Debug mode is enabled");
      console.log("%c%s", "color: red;font-size: 18px;", "Admin mode is " + this.get("enabled"));
    }
  } //getter and setter


  _createClass(Info, [{
    key: "set",
    value: function set(name, value) {
      this[name] = value;
    }
  }, {
    key: "get",
    value: function get(name) {
      return this[name];
    }
  }]);

  return Info;
}();

var Focus = function Focus() {
  _classCallCheck(this, Focus);

  $('.js-focus').focus();
};

var main = /*#__PURE__*/function () {
  function main() {
    var _this = this;

    _classCallCheck(this, main);

    // register starthandler
    document.addEventListener('app-loaded', function () {
      _this.loaded();
    });
  }

  _createClass(main, [{
    key: "load",
    value: function load() {
      // init all needed preloads
      console.debug("App init");
      var loaded = new CustomEvent("app-loaded");
      document.dispatchEvent(loaded);
    }
  }, {
    key: "loaded",
    value: function loaded() {
      // at this Point Page is ready
      this.infoObj = new Info(); //instantiate a script

      this.focusObj = new Focus();
      console.debug("App loaded");
    }
  }]);

  return main;
}(); // global Variables


var app;
var timeStart = performance.now(); //main handler

$(document).ready(function () {
  app = new main();
  window.top["app"] = app; // reassign for global usage

  app.load();

  if (app.info.get("isDebug")) {
    var timeEnd = performance.now();
    console.debug("Loaded App in " + (timeEnd - timeStart) + " milliseconds.");
  }
});