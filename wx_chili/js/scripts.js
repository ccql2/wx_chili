document.addEventListener('DOMContentLoaded', () => {
    const simulateScanButton = document.getElementById('simulate-scan');
    const productInfoSection = document.getElementById('product-info');
    const productDetailsContainer = document.getElementById('product-details');

    simulateScanButton.addEventListener('click', () => {
        // 模拟扫描后显示产品信息
        const mockProductData = {
            name: '特辣五号辣椒',
            origin: '四川成都',
            packagingDate: '2023-10-01',
            logisticsStatus: '已发货',
            description: '这是一款非常辣的辣椒，适合喜欢辣味的朋友。'
        };

        displayProductInfo(mockProductData);
    });

    function displayProductInfo(productData) {
        productInfoSection.style.display = 'block';
        productDetailsContainer.innerHTML = `
            <h3>${productData.name}</h3>
            <p><strong>产地：</strong>${productData.origin}</p>
            <p><strong>包装日期：</strong>${productData.packagingDate}</p>
            <p><strong>物流状态：</strong>${productData.logisticsStatus}</p>
            <p><strong>描述：</strong>${productData.description}</p>
        `;
    }
});