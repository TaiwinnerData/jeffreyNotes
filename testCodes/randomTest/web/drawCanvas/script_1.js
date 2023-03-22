   const canvas = document.getElementById('canvas');
      const ctx = canvas.getContext('2d');
      const compressedCanvas = document.getElementById('compressed-canvas');
      const compressedCtx = compressedCanvas.getContext('2d');
      
      // Set up brush parameters
      let brushSize = 5;
      let brushColor = 'black';
      let brushOpacity = 1;
      
      // Set up mouse event listeners
      let isDrawing = false;
      let lastX = 0;
      let lastY = 0;
      
      canvas.addEventListener('mousedown', (e) => {
        isDrawing = true;
        lastX = e.offsetX;
        lastY = e.offsetY;
      });
      
      canvas.addEventListener('mousemove', (e) => {
        if (isDrawing) {
          drawLine(lastX, lastY, e.offsetX, e.offsetY);
          lastX = e.offsetX;
          lastY = e.offsetY;
        }
      });
      
      canvas.addEventListener('mouseup', () => {
        isDrawing = false;
        compress();
      });
      
      // Set up brush controls
      const brushSizeInput = document.createElement('input');
      brushSizeInput.type = 'range';
      brushSizeInput.min = '1';
      brushSizeInput.max = '10';
      brushSizeInput.step = '1';
      brushSizeInput.value = brushSize.toString();
      brushSizeInput.addEventListener('input', (e) => {
        brushSize = parseInt(e.target.value);
      });
      
      const brushColorInput = document.createElement('input');
      brushColorInput.type = 'color';
      brushColorInput.value = brushColor;
      brushColorInput.addEventListener('input', (e) => {
        brushColor = e.target.value;
      });
      
      const brushOpacityInput = document.createElement('input');
      brushOpacityInput.type = 'range';
      brushOpacityInput.min = '0';
      brushOpacityInput.max = '1';
      brushOpacityInput.step = '0.1';
      brushOpacityInput.value = brushOpacity.toString();
      brushOpacityInput.addEventListener('input', (e) => {
        brushOpacity = parseFloat(e.target.value);
      });
      
      const brushControlsDiv = document.createElement('div');
      brushControlsDiv.appendChild(brushSizeInput);
      brushControlsDiv.appendChild(brushColorInput);
      brushControlsDiv.appendChild(brushOpacityInput);
      document.body.appendChild(brushControlsDiv);
      
      // Helper function to draw a line from (x1, y1) to (x2, y2)
      function drawLine(x1, y1, x2, y2) {
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.strokeStyle = brushColor;
        ctx.lineWidth = brushSize;
        ctx.lineCap = 'round';
        ctx.globalAlpha = brushOpacity;
        ctx.stroke();
        ctx.closePath();
      }

	function compress() {
		const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        	const compressedData = compressedCtx.createImageData(compressedCanvas.width, compressedCanvas.height);
    
	    // Loop through every pixel in the compressed image
	    for (let y = 0; y < compressedCanvas.height; y++) {
	      for (let x = 0; x < compressedCanvas.width; x++) {
		// Compute the average color of the corresponding 8x8 pixel block in the original image
		let sumR = 0;
		let sumG = 0;
		let sumB = 0;
		let sumA = 0;
		for (let j = 0; j < 8; j++) {
		  for (let i = 0; i < 8; i++) {
		    const pixelIndex = ((y * 8 + j) * canvas.width + (x * 8 + i)) * 4;
		    const pixelR = imageData.data[pixelIndex];
		    const pixelG = imageData.data[pixelIndex + 1];
		    const pixelB = imageData.data[pixelIndex + 2];
		    const pixelA = imageData.data[pixelIndex + 3];
		    sumR += pixelR;
		    sumG += pixelG;
		    sumB += pixelB;
		    sumA += pixelA;
		  }
		}
		const avgR = Math.round(sumR / 64);
		const avgG = Math.round(sumG / 64);
		const avgB = Math.round(sumB / 64);
		const avgA = Math.round(sumA / 64);
		
		// Set the corresponding pixel in the compressed image to the average color
		const compressedIndex = (y * compressedCanvas.width + x) * 4;
		compressedData.data[compressedIndex] = avgR;
		compressedData.data[compressedIndex + 1] = avgG;
		compressedData.data[compressedIndex + 2] = avgB;
		compressedData.data[compressedIndex + 3] = avgA;

		}
	    }
    // Update the compressed image
    compressedCtx.putImageData(compressedData, 0, 0);
  }

