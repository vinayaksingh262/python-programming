<!DOCTYPE html >
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		body {
			background-color: #1D1F21;
			color: darkgray;
			font-family: Arial, Helvetica, sans-serif;
			align-items: center;
			justify-content: center;
			display: flex;
			flex-direction: column;
		}

		.hidden {
			display: none;
		}

		.originalImage {
			height: 300px;
			width: 300px;
			margin-left: 20px;
			margin-right: 20px;
			border: #bac4ce00 solid;
			background-color: rgba(127, 255, 212, 0);
		}

		canvas {
			width: 300px;
			height: 300px;
		}

		.result {
			display: none;
			flex-direction: row;
			width: 100%;
			align-items: center;
			justify-content: center;
		}

		.cols {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			margin: 20px;
		}

		@media screen and (max-width: 650px) {
			.result {
				flex-direction: column;
			}
		}

		.options {
			display: flex;
			justify-content: center;
			align-items: center;
		}

		button {
			margin: 10px;
		}

		img {
			height: 300px;
			width: 300px;
		}

		.data-extracted {
			display: none;
			flex-direction: column;
			align-items: center;
			justify-content: space-between;
		}
	</style>
</head>
<body >


	<h1>Steganography Project</h1>
	<hr width="100%">
	<h3>
		Steganography is the practice of representing information within another message or physical object, in such a manner that the presence of the information is not evident to human inspection.<br><br>
		Image Steganography.
	</h3>
	<hr width="100%">
	<h2>Enter text to hide in image</h2>
	<textarea rows="4" cols="40" class="content" placeholder="Enter text to hide" style="resize: none;"></textarea>
	<h2>
		<label for="files" class="labelFiles">Choose File :</label>
		<input type="file" id="files" accept="image/*" placeholder="hell"/>
	</h2>
	<div class="options">
		<button class="encrypt"><h2>Hide the message</h2></button>
		<button class="extract"><h2>Extract message</h2></button>
	</div>
	<div class="result">
		<div class="cols">
			<h2>Before Modification</h2>
			<img src="" class="originalImage">
		</div>
		<div class="cols">
			<h2>After Modification</h2>
			<canvas id="imageCanvas"></canvas>
		</div>
	</div>
	<button class="download hidden" href="" download><h2>DOWNLOAD</h2></button>
	<div class="data-extracted hidden">
		<h2>Selected image</h2>
		<canvas id="imageCanvas2"></canvas>
		<h2>Hidden data</h2>
		<div class="notice" style="color:red; display:none">
			no hidden data / (make sure you are using the downloaded file for extraction)
		</div>
		<textarea rows="4" cols="40" class="extracted-item" placeholder="hidden data" style="resize: none;"></textarea>
	</div>
	<script>
		let file_uploded = 0;
		let imageCanvas = document.querySelector('#imageCanvas');
		const fileInput = document.querySelector("#files");

		fileInput.addEventListener('change', (event) => {
			file_uploded = 1;
			let selectedFile = event.target.files[0];
			const url = URL.createObjectURL(selectedFile);
			document.querySelector('.originalImage').src = url;
			document.querySelector('.originalImage').classList.remove('hidden');
		});

		const encrypt = document.querySelector('.encrypt');

		encrypt.addEventListener('click', () => {
			if (file_uploded === 1) {
				createImageCanvas();
				document.querySelector('.download').style.display = "block";
				document.querySelector('.result').style.display = "flex";
				document.querySelector('.data-extracted').style.display = "none";
			} else alert("select image file");
		});

		function createImageCanvas() {
			let img = new Image();
			img.src = URL.createObjectURL(fileInput.files[0]);
			img.onload = function () {
				imageCanvas.width = img.width;
				imageCanvas.height = img.height;
				const ctx = imageCanvas.getContext("2d");
				ctx.drawImage(img, 0, 0);
				const imageData = ctx.getImageData(0, 0, imageCanvas.width, imageCanvas.height);
				const pixelData = imageData.data;
				let message = document.querySelector('.content').value;
				message = ("Valid\n" + message);
				for (let i = 0; ((i < pixelData.length)); i += 1) {
					pixelData[i] &= 252;
				}

				const arr = [];
				for (let i = 0; i < message.length; i++) {
					let x = message[i].charCodeAt(0);
					let a = 128;
					while (a > 0) {
						if (((a & x) === a)) {
							arr.push(1);
						} else arr.push(0);
						a >>= 1;
					}
				}

				let ctr = 0;
				for (let i = 0; i < arr.length; i += 2) {
					pixelData[ctr] += (2 * arr[i] + arr[i + 1]);
					ctr++;
				}

				ctx.putImageData(imageData, 0, 0);
			}

			document.querySelector('.download').addEventListener('click', () => {
				imageCanvas.toBlob(function (blob) {
					const downloadLink = document.createElement('a');
					downloadLink.download = 'myCanvasImage.png';
					const url = URL.createObjectURL(blob);
					downloadLink.href = url;
					downloadLink.click();
					URL.revokeObjectURL(url);
				}, 'image/png');
			});

			const download = document.querySelector('.download');
			download.href = img.src;
		}

		document.querySelector('.extract').addEventListener('click', () => {
			if (file_uploded === 1) {
				document.querySelector('.result').style.display = "none";
				document.querySelector('.download').style.display = "none";
				document.querySelector('.data-extracted').style.display = "flex";

				let imageCanvas2 = document.querySelector('#imageCanvas2');
				let img = new Image();
				img.src = URL.createObjectURL(fileInput.files[0]);
				img.onload = function () {
					imageCanvas2.width = img.width;
					imageCanvas2.height = img.height;
					let ctxt = imageCanvas2.getContext("2d");
					ctxt.drawImage(img, 0, 0);
					let imageData = ctxt.getImageData(0, 0, imageCanvas2.width, imageCanvas2.height);
					const pixelData = imageData.data;
					const data_wali_array = [];
					for (let i = 0; i < pixelData.length; i++) {
						data_wali_array.push((((pixelData[i] & 2) != 0) ? 1 : 0));
						data_wali_array.push(pixelData[i] & 1);
					}

					let ans = "";
					let x = 0;
					let flag = 1;
					for (let i = 0; i < data_wali_array.length; i++) {
						let a = 1;
						if (data_wali_array[i] == 1) {
							a <<= (7 - i % 8);
							x += a;
						}
						if (i % 8 === 7) {
							if (String.fromCharCode(x) === '\0') {
								break;
							}
							x %= 128;
							ans += String.fromCharCode(x);
							x = 0;
						}
						if (ans.length === 5 && ans !== "Valid") {
							document.querySelector('.extracted-item').value = "";
							document.querySelector('.notice').style.display = "block";
							console.log("not encoded" + ans);
							flag = 0;
							break;
						}
					}
					if (flag) {
						document.querySelector('.notice').style.display = "none";
						document.querySelector('.extracted-item').value = ans.substring(6);
					}
				}
			} else alert("select image file");
		});
	</script>
</body>
</html>
