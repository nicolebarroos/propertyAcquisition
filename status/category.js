(function($) {
    $(function() {
        var status = $('#status'),
            informations = $('#id_informacoes');

        function toggleVerified(value) {
            value == "Em análise" ? informations.show() : informations.hide();
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(status.val());

        // show/hide on change
        status.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);