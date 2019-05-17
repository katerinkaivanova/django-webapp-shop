window.onload = function () {
    var _quantity, _price, orderitemNum, deltaQuantity, orderitemQuantity, delta_cost;
    var quantityArr = [];
    var priceArr = [];

    var totalForms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());

    var orderTotalQuantity = parseInt($('.order_total_quantity').text()) || 0;
    var orderTotalCost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;
    var $orderForm = $('.order_form');

    for (i = 0; i < totalForms; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantityArr[i] = _quantity;
        if (_price) {
            priceArr[i] = _price;
        } else {
            priceArr[i] = 0;
        }
    }

    if (!orderTotalQuantity) {
        for (i = 0; i < totalForms; i++) {
            orderTotalQuantity += quantityArr[i];
            orderTotalCost += quantityArr[i] * priceArr[i];
        }
        $('.order_total_quantity').html(orderTotalQuantity.toString());
        $('.order_total_cost').html(Number(orderTotalCost.toFixed(2)).toString());
    }

    function orderSummaryUpdate(orderitemPrice, deltaQuantity) {
        delta_cost = orderitemPrice * deltaQuantity;
        orderTotalCost = Number((orderTotalCost + delta_cost).toFixed(2));
        orderTotalQuantity = orderTotalQuantity + deltaQuantity;

        $('.order_total_cost').html(orderTotalCost.toString());
        $('.order_total_quantity').html(orderTotalQuantity.toString());
    }

    function deleteOrderItem(row) {
        var targetName = row[0].querySelector('input[type="number"]').name;
        orderitemNum = parseInt(targetName.replace('orderitems-', '').replace('-quantity', ''));
        deltaQuantity = -quantityArr[orderitemNum];
        orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
    }

    $orderForm.on('change', 'input[type="number"]', function (event) {
        var target = event.target;
        orderitemNum = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (priceArr[orderitemNum]) {
            orderitemQuantity = parseInt(target.value);
            deltaQuantity = orderitemQuantity - quantityArr[orderitemNum];
            quantityArr[orderitemNum] = orderitemQuantity;
            orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
        }
    });

    $orderForm.on('change', 'input[type="checkbox"]', function (event) {
        var target = event.target;
        orderitemNum = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
        if (target.checked) {
            deltaQuantity = -quantityArr[orderitemNum];
        } else {
            deltaQuantity = quantityArr[orderitemNum];
        }
        orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
    });

    $('.formset_row').formset({
        addText: 'add product',
        deleteText: 'delete',
        prefix: 'orderitems',
        removed: deleteOrderItem
    });

    $('.order_form').on('change','select',function (event) {
        var target = event.target;
        console.log(target);
    });
};