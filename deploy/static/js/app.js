// Adds a page load event that replaces "img.js-svg"-tags by an embedded version of the image.
// As fetch()
window.addEventListener(
	"load",
	() => {
		let domParser = new DOMParser();
		let embedSvgs = document.querySelectorAll("img.js-svg");

		for( let embedSvg of embedSvgs ) {
			fetch(embedSvg["src"])
				.then(response => response.text())
				.then(svg => {
					if( !svg )
						return;

					var svgElement = domParser.parseFromString(svg, "image/svg+xml");
					svgElement = svgElement.querySelector("svg");

					svgElement.classList = embedSvg.classList;
					embedSvg.replaceWith(svgElement);
				})
				.catch();
		}
	}
);
