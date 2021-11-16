(function($) {
    $(function() {
        var status = $('#id_status'),
            valor_financiamento = $('#id_valor_financiamento');

        function toggleVerified(value) {
            value == "2" ? valor_financiamento.show() : valor_financiamento.hide();
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(status.val());

        // show/hide on change
        status.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);