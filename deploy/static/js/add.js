window.onload = () => {
	init();
}

function init() {
	document.querySelectorAll(".js-viur-bones-file-upload-file-button").forEach((addButton) => {
		addButton.addEventListener("click", addButtonClick)
	})
}

function addButtonClick(event) {
	//Shadow File Opener
	var shadowfile = document.createElement("input");
	shadowfile.type = "file";
	shadowfile.click();
	shadowfile.addEventListener("change", (e) => {
		const file = e.target.files[0];

		getUploadUrl(file).then(uploadData => {
			uploadFile(file, uploadData).then(resp => {
				const parent = event.target.parentElement;
				const inputName = parent.dataset["name"];
				const keyinput = parent.querySelector('[name="' + inputName + '"]');
				addFile(uploadData,keyinput)

			});
		});
	});


}

function getUploadUrl(file) {
	return new Promise((resolve, reject) => {
		getSkey().then(skey => {

			let data = {
				"fileName": file.name,
				"mimeType": file.type,
				"size": file.size,
				"skey": skey,
			}
			fetch("/json/file/getUploadURL", {
				method: 'POST',
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded',
				},
				body: new URLSearchParams(data).toString()
			}).then(response => response.json()).then((data) => resolve(data))
		})
	});
}

function uploadFile(file, uploadData) {

	return new Promise((resolve, reject) => {
		fetch(uploadData["values"]["uploadUrl"], {
			method: "POST",
			body: file,
			mode: "no-cors",

		}).then(response => {
			resolve(response)
		})
	})

}

function addFile(uploadData, keyinput) {
	var currentUpload = {}
	return new Promise((resolve, reject) => {
		currentUpload["key"] = uploadData["values"]["uploadKey"];
		currentUpload["node"] = undefined;
		currentUpload["skelType"] = "leaf";
		getSkey().then(skey => {
			currentUpload["skey"] = skey;
			fetch("/json/file/add", {
				method: "POST",
				headers: {
					'Content-Type': 'application/x-www-form-urlencoded',
				},
				mode: "no-cors",
				body: new URLSearchParams(currentUpload).toString(),
			}).then(
				response => response.json()).then((data) => {

				keyinput.value = data.values.key;
			});
		});
	});
}

function getSkey() {
	return new Promise((resolve, reject) => {
		fetch("/json/skey", {method: 'POST'})
			.then(response => response.json())
			.then(data => resolve(data));
	});
}
