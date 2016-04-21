$(document).ready(function() {
    $("#votar").click(function() {
        var restaurante = $("#restaurante").data("nombre");

        $.getJSON("/app/votar/?restaurante=" + restaurante, function(result) {
          $("#voto").val(result.votos);
        });
    });
});
