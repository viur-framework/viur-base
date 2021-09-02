// Adds a page load event that replaces "img.js-svg"-tags by an embedded version of the scalable vector graphic.
window.addEventListener(
	"load",
	() => {
		let domParser = new DOMParser();  // Will be used later.
		let embedSvgs = document.querySelectorAll("img.js-svg"); // Select all img-elements with 'js-svg'-class

		for (let embedSvg of embedSvgs) {
			fetch(embedSvg["src"])  // Fetch the src of the img-element. This should hit the cache after first page load.
				.then(response => response.text())
				.then(svg => {
					if (!svg) // Skip empty content
						return;

					// Turn fetched svg code into a dom...
					var svgElement = domParser.parseFromString(svg, "image/svg+xml");

					// ...and ensure to find the svgs's root node, which will be inserted into the main DOM
					if (svgElement && (svgElement = svgElement.querySelector("svg"))) {
						svgElement.classList = embedSvg.classList;  // Take all classes from the img-element
						embedSvg.replaceWith(svgElement); // Embed the SVG in place of the img-element
					}
				});
		}
	}
);
