$(document).ready(function () {

    $(document).on("click", ".add-to-cart", function (e) {

        e.preventDefault();

        var product_id = $(this).data("product-id");

        var add_to_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },


            error: function (data) {
                console.log("Error couldnt add item to cart");
            },
        });
    });




    $(document).on("click", ".remove-from-cart", function(e) {

        e.preventDefault();

        var cart_id = $(this).data("cart-id");

        var remove_from_cart = $(this).attr("href");

        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (data) {
                console.log("Error removing item from cart");
            },
        });
    });




    $(document).on("click", ".decrement", function () {
        // ����� ������ �� ���������� django �� �������� data-cart-change-url
        var url = $(this).data("cart-change-url");
        // ����� id ������� �� �������� data-cart-id
        var cartID = $(this).data("cart-id");
        // ���� ���������� input � ����������� 
        var $input = $(this).closest('.input-group').find('.number');
        // ����� �������� ���������� ������
        var currentValue = parseInt($input.val());
        // ���� ���������� ������ ������, �� ������ ����� ������ -1
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            // ��������� ������� ������������ ����
            // � ����������� (id �����, ����� ����������, ���������� ����������� ��� �����������, url)
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    // ���������� ������� ��� ���������� ��������
    $(document).on("click", ".increment", function () {
        // ����� ������ �� ���������� django �� �������� data-cart-change-url
        var url = $(this).data("cart-change-url");
        // ����� id ������� �� �������� data-cart-id
        var cartID = $(this).data("cart-id");
        // ���� ���������� input � ����������� 
        var $input = $(this).closest('.input-group').find('.number');
        // ����� �������� ���������� ������
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);

        // ��������� ������� ������������ ����
        // � ����������� (id �����, ����� ����������, ���������� ����������� ��� �����������, url)
        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                // ���������
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // ����� 7��� ������� ���������
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // �������� ���������� ������� � �������
                var goodsInCartCount = $("#goods-in-cart-count");
                var cartCount = parseInt(goodsInCartCount.text() || 0);
                cartCount += change;
                goodsInCartCount.text(cartCount);

                // ������ ���������� �������
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("������ ��� ���������� ������ � �������");
            },
        });
    }

});