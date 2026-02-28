// Barcode data (converted from your JSON)
const barcodes = {
    "123456789012": {
      "name": "Genuine Headphones",
      "brand": "AudioPlus",
      "status": "genuine"
    },
    "987654321098": {
      "name": "Fake Watch",
      "brand": "FauxTime",
      "status": "fake"
    }
  };
  
  // Main verification function
  function verifyBarcode() {
    const input = document.getElementById("barcodeInput").value.trim();
    const resultDiv = document.getElementById("result");
  
    if (!input) {
      resultDiv.innerHTML = "<p>Please enter a barcode.</p>";
      return;
    }
  
    const product = barcodes[input];
  
    if (product) {
      resultDiv.innerHTML = `
        <h3>Verification Result</h3>
        <p><strong>Product:</strong> ${product.name}</p>
        <p><strong>Brand:</strong> ${product.brand}</p>
        <p><strong>Status:</strong> <span style="color:${product.status === 'genuine' ? 'green' : 'red'}">${product.status.toUpperCase()}</span></p>
      `;
    } else {
      resultDiv.innerHTML = "<p style='color:orange;'>Product not found!</p>";
    }
  }