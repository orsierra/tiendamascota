$("#btn-cargar").click(function (event) {
  event.preventDefault();
  var url = "https://api.punkapi.com/v2/beers/random";
    fetch(url)
        .then(response => response.json())
        .then(data => 
            {
                var $nombre_cerveza = $('<h1>').text(data[0].name);
                var $eslogan = $('<p>').text("Eslogan: "+data[0].tagline)
                var $grados = $('<p>').text("Grados: "+data[0].abv);
                var $descripcion = $('<p>').text("Información: "+data[0].description);
                var $creacion = $('<p>').text("Fecha de creación: "+data[0].first_brewed);
                var $acompañamiento = $('<p>').text("Acompañamientos recomendados: "+data[0].food_pairing);
                var $foto_cerveza = $("<p><img src='"+data[0].image_url+"'>");
                $("#info").empty();
                $('#info')
                    .append($nombre_cerveza)
                    .append($eslogan)
                    .append($grados)
                    .append($descripcion)
                    .append($creacion)
                    .append($acompañamiento)
                    .append($foto_cerveza);
            })
        .catch(error => console.error(error));
});
