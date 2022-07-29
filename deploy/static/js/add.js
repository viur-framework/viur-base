window.onload = () => {
	init();
}

function init() {
	document.querySelectorAll(".js-viur-bones-file-upload-file-button").forEach((addButton) => {
		console.log()
		if (addButton.parentElement.dataset.multiple === "0") {
			addButton.addEventListener("click", addButtonClick)
		} else //Multiple value
		{
			const addMultipleBtn = document.querySelector(".js-viur-bones-file-add-files");
			addMultipleBtn.addEventListener("click", (event) => {
				const newElement = event.target.parentElement.querySelector(".vi-file").cloneNode(true);
				//clear new element
				console.log(newElement)
				const boneName = newElement.dataset.name;
				newElement.querySelector('[name="' + boneName + '"]').value = "";
				newElement.querySelector(".input").innerText = "";

				event.target.parentElement.querySelector(".vi-file").parentElement.appendChild(newElement);
				newElement.querySelectorAll(".js-viur-bones-file-upload-file-button").forEach((addButton) => {

					addButton.addEventListener("click", addButtonClick)
				});

			})
			addButton.addEventListener("click", addButtonClick)
		}
	})
	document.querySelectorAll(".js-viur-bones-file-remove-file").forEach((cancelButton) => {
		cancelButton.addEventListener("click", () => {
			const boneName = cancelButton.parentElement.dataset.name;
			cancelButton.parentElement.querySelector('[name="' + boneName + '"]').value = "";
			cancelButton.parentElement.querySelector(".input").innerText = "";
		})
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

			const parent = event.target.parentElement;
			const inputspan = parent.querySelector('.input');
			inputspan.innerText="Uploading..."
			uploadFile(file, uploadData).then(resp => {

				const inputName = parent.dataset["name"];
				const keyinput = parent.querySelector('[name="' + inputName + '"]');

				addFile(uploadData, keyinput, inputspan)

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

function addFile(uploadData, keyinput, inputSpan) {
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
				//Refresh skey
				const skeyInput = document.querySelector('[name="skey"]');
				console.log(skeyInput)
				inputSpan.innerText = "Upload done."
				if (skeyInput !== null) {
					getSkey().then((skey) => {
						skeyInput.value = skey;
					})

				}
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
